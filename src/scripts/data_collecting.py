import numpy as np
import time
import cv2

from scripts.utils import *


def start_data_collecting_mode():
    print("[INFO] Entered data collecting mode...")
    captured_video = cv2.VideoCapture(0)

    draw_area_points = {
            'point1': (800, 100),  'point2': (800, 500), 
            'point3': (1200, 500), 'point4': (1200, 100)
    }
    key_options = [('a', 'toggle drawing'), ('s', 'save image')]
    font        = cv2.FONT_HERSHEY_SIMPLEX
    key_option_colors = [(0, 255, 0), (0, 255, 0)]

    capture_drawing_status = False

    while True:
        ret, video_frame  = captured_video.read()
        video_frame       = cv2.flip(video_frame, 1)
        video_frame       = draw_area(video_frame, draw_area_points, (0, 255, 0), 6)
        video_frame       = draw_key_options(video_frame, key_options, font, key_option_colors)
        white_image       = create_white_image()
        video_frame_clone = video_frame.copy()

        key_events = cv2.waitKey(1) & 0xFF

        if key_events == ord('q'):
            print("[INFO] Exiting data collecting mode...")
            print("[INFO] Closed")
            break
        elif key_events == ord('a'):
            capture_drawing_status, key_option_colors = toggle_key_a(capture_drawing_status)

        cv2.imshow("video", video_frame)
        cv2.imshow("white frame", white_image)

    cv2.destroyAllWindows() 
    
