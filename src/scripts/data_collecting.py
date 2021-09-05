import numpy as np
import time
import cv2

from scripts.utils import *


key_option_colors = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]
center_dots = []


def key_s_on_click(image, save_path):
    print("[INFO] Saving drawn image...")
    global key_option_colors
    key_option_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 0)]
    ImageProcessing().save_image(image, save_path, 64, 64, resize=True)
    key_c_on_click()
    print("[INFO] Drawn image saved")
    key_option_colors = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]


def key_c_on_click():
    print("[INFO] Clearing drawn image...")
    global key_option_colors, center_dots
    key_option_colors = [(0, 255, 0), (0, 255, 0), (255, 0, 0)]
    center_dots.clear()
    print("[INFO] Drawn image cleared")
    key_option_colors = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]


def start_data_collecting_mode(save_path):
    global key_option_colors, center_dots
    
    print("[INFO] Entered data collecting mode...")
    captured_video = cv2.VideoCapture(0)

    draw_area_points = {
            'point1': (800, 100),  'point2': (800, 500), 
            'point3': (1200, 500), 'point4': (1200, 100)
    }
    key_options = [('a', 'toggle drawing'), ('s', 'save image'), ('c', 'clear screen')]
    font        = cv2.FONT_HERSHEY_SIMPLEX
    position    = 'vertical'
    capture_drawing_status = False

    while True:
        ret, video_frame  = captured_video.read()
        video_frame       = cv2.flip(video_frame, 1)
        video_frame       = draw_area(video_frame, draw_area_points, (0, 255, 0), 6)
        video_frame       = draw_key_options(position, video_frame, key_options, font, key_option_colors)
        video_frame       = draw_save_count(save_path, video_frame, font, (255, 255, 0))
        video_frame_clone = video_frame.copy()
        white_image       = create_white_image()
        white_image1       = create_white_image()
        white_image2       = create_white_image()
        white_image3       = create_white_image()
        white_image4       = create_white_image()
        white_image5       = create_white_image()
        white_image6       = create_white_image()
        white_image7       = create_white_image()
        white_image8       = create_white_image()
        white_image9       = create_white_image()
        center_dots       = drawing_on_air(
            video_frame, 
            video_frame_clone, 
            white_image, 
            white_image1,
            white_image2,
            white_image3,
            white_image4,
            white_image5,
            white_image6,
            white_image7,
            white_image8,
            white_image9,
            draw_area_points,
            capture_drawing_status, center_dots
        )
        key_events = cv2.waitKey(1) & 0xFF

        if key_events == ord('q'):
            print("[INFO] Exiting data collecting mode...")
            print("[INFO] Closed")
            break
        elif key_events == ord('a'): 
            capture_drawing_status, key_option_colors = toggle_key_a(capture_drawing_status)
        elif key_events == ord('s'): key_s_on_click(white_image, save_path)
        elif key_events == ord('c'): key_c_on_click()

        cv2.imshow("Data collecting mode", video_frame)
        cv2.imshow("white frame", white_image)
        cv2.imshow("white frame1", white_image1)
        cv2.imshow("white frame2", white_image2)
        cv2.imshow("white frame3", white_image3)
        cv2.imshow("white frame4", white_image4)
        cv2.imshow("white frame5", white_image5)
        cv2.imshow("white frame6", white_image6)
        cv2.imshow("white frame7", white_image7)
        cv2.imshow("white frame8", white_image8)
        cv2.imshow("white frame9", white_image9)

    cv2.destroyAllWindows() 
