import os
import numpy as np
import cv2


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


def draw_save_count(frame, count, coordinate, font, color):
    # count is the number of count display on screen
    # coordinate: tuple of coordinate x and y
    if count is not None:
        cv2.putText(frame, f'Image {count} saved', 
                    coordinate, font, 1, color, 2, cv2.LINE_AA)
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


def save_image():
    pass 


def clear_drawn_image():
    pass


def resize_image(image):
    pass
