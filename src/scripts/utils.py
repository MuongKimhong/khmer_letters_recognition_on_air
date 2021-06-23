import os
import cv2
import numpy as np
from imutils import paths


# use blue color to draw on air
def find_blue_color(hsv_frame, original_frame):
    kernel    = np.ones((5, 5), np.uint8)
    low_red   = np.array([112, 100, 20])
    high_red  = np.array([129, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_red, high_red)
    blue_mask = cv2.erode(blue_mask, kernel, iterations=2)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
    blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)
    return blue_mask


def draw_area(frame, draw_points, color, thickness):
    # draw_points is the dict of points, eg. {'point1': (800, 1000), ...}
    cv2.line(frame, draw_points['point1'], draw_points['point2'], color, thickness)
    cv2.line(frame, draw_points['point2'], draw_points['point3'], color, thickness)
    cv2.line(frame, draw_points['point3'], draw_points['point4'], color, thickness)
    cv2.line(frame, draw_points['point4'], draw_points['point1'], color, thickness)
    return frame


def draw_key_options(position, frame, key_options, font, option_colors):
    # key_options is list of tuples of key options, eg. [("a", "draw or pause"), ("s", "save images")]

    # option_colors is the list of color for options and same order as key_options:
    # [(0, 155, 0), (100, 255, 100), ..]
    if position != 'horizontal' and position != 'vertical':
        exception = '''
        position argument accepts keyword <horizontal> or <vertical> 
        but {} was given
        '''.format(position)
        raise Exception(exception)
        
    if position == 'horizontal':
        cv2.putText(frame, f'- Press {key_options[0][0]} to {key_options[0][1]}', 
                   (40, 50), font, 0.8, option_colors[0], 2, cv2.LINE_AA)
        cv2.putText(frame, f'- Press {key_options[1][0]} to {key_options[1][1]}', 
                   (480, 50), font, 0.8, option_colors[1], 2, cv2.LINE_AA)
        cv2.putText(frame, f'- Press {key_options[2][0]} to {key_options[2][1]}',
                   (900, 50), font, 0.8, option_colors[2], 2, cv2.LINE_AA)
    elif position == 'vertical':
        cv2.putText(frame, f'- Press {key_options[0][0]} to {key_options[0][1]}',
                   (40, 150), font, 0.8, option_colors[0], 2, cv2.LINE_AA)
        cv2.putText(frame, f'- Press {key_options[1][0]} to {key_options[1][1]}',
                   (40, 250), font, 0.8, option_colors[1], 2, cv2.LINE_AA)
        cv2.putText(frame, f'- Press {key_options[2][0]} to {key_options[2][1]}',
                   (40, 350), font, 0.8, option_colors[2], 2, cv2.LINE_AA)
    return frame


def save_image(save_to_path, image, image_name):
    save_dir   = os.listdir(save_to_path)
    file_count = len([file for file in save_dir if os.path.isfile(file)])   
    
    print("[INFO] saving image {}".format(file_count + 1))
    cv2.imwrite(save_to_path + "{}{}.jpg".format(image_name, file_count + 1))
    return {'success': True}


def create_white_image(size=[400, 400]):
    image = np.zeros(size, dtype=np.uint8)
    image.fill(255)
    return image


def toggle_key_a(capture_drawing_status):
    if not capture_drawing_status:
        print("[INFO] Capture drawing")
        capture_drawing_status = True
        option_colors  = [(255, 0, 0), (0, 255, 0), (0, 255, 0)]
    else:
        print("[INFO] Stop capture drawing")
        capture_drawing_status = False
        option_colors  = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]
    return (capture_drawing_status, option_colors)


def drawing_on_air(video_frame, video_frame_clone, white_image, draw_area, capture_status, center_dots):
    hsv_area  = [draw_area['point1'][1], draw_area['point3'][1], 
                 draw_area['point1'][0], draw_area['point3'][0]]
    hsv_frame = cv2.cvtColor(video_frame_clone, cv2.COLOR_BGR2HSV) 
    blue_mask = find_blue_color(hsv_frame[hsv_area[0]:hsv_area[1], hsv_area[2]:hsv_area[3]], 
                                video_frame_clone)
    (contour, _) = cv2.findContours(blue_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # check if any countours were found
    if len(contour) > 0:
        contour          = sorted(contour, key=cv2.contourArea, reverse=True)[0]
        ((x, y), radius) = cv2.minEnclosingCircle(contour)

        # draw circle around contour and draw circle only in draw area
        cv2.circle(video_frame[hsv_area[0]:hsv_area[1], hsv_area[2]:hsv_area[3]], 
                  (int(x), int(y)), int(radius), (0, 255, 0), 2)

        # Find center of countour
        moment = cv2.moments(contour)
        center = [(int(moment['m10'] / moment['m00'])) + 800, (int(moment['m01'] / moment['m00'])) + 100]
        cv2.circle(video_frame, (center[0], center[1]), 12, (255, 255, 255), -1)

        if capture_status: center_dots.append(center)

    for center_dot in center_dots:
        if (center_dot[0] > 800 and center_dot[0] < 1200) and (center_dot[1] > 100 and center_dot[1] < 500):
            # coordinates to draw on white image
            circle_coordinate_x = center_dot[0] - 800 - 5
            circle_coordinate_y = center_dot[1] - 100 - 5
            
            cv2.circle(video_frame, (center_dot[0] - 5, center_dot[1] - 5), 12, (255, 255, 0), -1)
            cv2.circle(white_image, (circle_coordinate_x, circle_coordinate_y),
                                        12, (0, 0, 0), -1)
    return center_dots


def draw_save_count(save_path, video_frame, font, color):
    total_images = len([image for image in os.listdir(save_path) if os.path.isfile(save_path + image)])
    cv2.putText(video_frame, f'{total_images} images saved', (880, 550), font, 0.8, color, 2,
                cv2.LINE_AA)
    return video_frame


class ImageProcessing:
    def get_total_files_in_dir(self, dir_path):
        return len([_file for _file in os.listdir(dir_path) if os.path.isfile(dir_path + _file)])

    # used to resize single image
    def resize_image(self, image, new_height, new_width):
        print("[INFO] Resizing image..")
        height, width = image.shape[:2] 
        padding_color = 0
        padding       = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        interpolation = cv2.INTER_AREA if (height > new_height) or (width > new_width) else cv2.INTER_CUBIC

        if len(image.shape) == 3 and not isinstance(padding_color, (list, tuple, np.ndarray)):
            padding_color = [padding_color] * 3

        resized_image = cv2.resize(image, (new_width, new_height), interpolation=interpolation)
        resized_image = cv2.copyMakeBorder(resized_image, padding['top'], padding['bottom'], padding['left'], 
                                           padding['right'], borderType=cv2.BORDER_CONSTANT, value=padding_color)
        return resized_image

    def save_image(self, image, save_path, image_width=None, image_height=None, resize=True): 
        if resize: 
            if (image_width is None) or (image_height is None):
                raise Exception("resize is set to True but width or height is not given")
            image = self.resize_image(image, image_width, image_height) 

        print(f"[INFO] Saving image into {save_path}")
        # total files inside provided save path
        total_files = self.get_total_files_in_dir(save_path)
        cv2.imwrite(save_path + f"image{total_files + 1}.jpg", image)
        print(f"[INFO] image{total_files + 1}.jpg saved")

    # used to resize images in one directory
    def resize_images_in_dir(self, dir_path, new_width, new_height):
        all_images = []

        for (index, image) in enumerate(list(paths.list_images(dir_path))):
            _image = cv2.imread(image, 0)
            resized_image = self.resize_image(_image, new_width, new_height)
            all_images.append(resized_image)
            # delete old image
            os.remove(image)

        # save all images from all_images list into save path directory 
        for image in all_images: self.save_image(image, dir_path, resize=False)

