# standard library import
import os
import argparse

# third party import
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils import paths
import numpy as np
import cv2

from scripts.data_collecting import (
    key_c_on_click,
    key_s_on_click
)
from scripts.utils import *

label = None
key_option_colors = [(9, 199, 9), (9, 199, 9), (9, 199, 9)]
center_dots = []


def key_c_on_click():
    print("[INFO] Clearing drawn image...")
    global key_option_colors, center_dots
    key_option_colors = [(0, 255, 0), (0, 255, 0), (255, 0, 0)]
    center_dots.clear()
    print("[INFO] Drawn image cleared")
    key_option_colors = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]


# key to predict
def key_p_on_click(model_path, images_to_save, save_path):
    global label

    class_labels = ['1_kor', '2_khor', '3_kur', '4_khur', '5_ngor', '6_chor', '7_chhor', '8_cher', '9_chher', '10_nger',
                    '11_dor', '12_thhor', '13_der', '14_ther', '15_nor', '16_thor', '17_tor', '18_thear', '19_thher',
                    '20_ner', '21_bor', '22_phor', '23_por', '24_pher', '25_mer', '26_yer', '27_ror', '28_lor', '29_vor', 
                    '30_sor', '31_hor', '32_lorl', '33_r']
    
    key_s_on_click(images_to_save, save_path)

    image_paths = list(paths.list_images(save_path))
    image_paths.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
    # print(image_paths)
    print(image_paths[-1])
    last_image_path = image_paths[-1]
    image = cv2.imread(last_image_path, 0)
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    print("[INFO] loading model .... ")
    pre_trained_model = load_model(model_path)
    print(pre_trained_model.predict(image))
    predicted_image = pre_trained_model.predict(image)[0]
    percentage = predicted_image

    index = np.where(predicted_image==max(predicted_image))
    index = index[0][0]
    label = class_labels[index]


def draw_predicted_label(video_frame):
    global label
    font = cv2.FONT_HERSHEY_SIMPLEX

    if label is not None:
        cv2.putText(video_frame, 'You wrote {}'.format(label), (890, 80), font, 1, (135, 0, 0), 2, cv2.LINE_AA)

    return video_frame


def start_predict_mode(model_path):
    global key_option_colors, center_dots

    save_path = '/Users/muongkimhong/Developments/khmer_letters_recognition_on_air/src/scripts/predicted_images/'

    print("[INFO] Entered predict mode...")
    captured_video = cv2.VideoCapture(0)

    draw_area_points = {
        'point1': (800, 100),  'point2': (800, 500), 
        'point3': (1200, 500), 'point4': (1200, 100)
    }
    key_options = [('a', 'toggle drawing'), ('p', 'predict'), ('c', 'clear screen')]
    font        = cv2.FONT_HERSHEY_SIMPLEX
    position    = 'vertical'
    capture_drawing_status = False

    while True:
        ret, video_frame  = captured_video.read()
        video_frame       = cv2.flip(video_frame, 1)
        video_frame       = draw_area(video_frame, draw_area_points, (0, 255, 0), 6)
        video_frame       = draw_key_options(position, video_frame, key_options, font, key_option_colors)
        video_frame       = draw_predicted_label(video_frame)
        video_frame_clone = video_frame.copy()
        white_image       = create_white_image()
        center_dots        = drawing_on_air(
            video_frame, 
            video_frame_clone, 
            draw_area_points,
            capture_drawing_status, 
            center_dots, 
            white_image
        )
        key_events = cv2.waitKey(1) & 0xFF

        if key_events == ord('q'):
            print("[INFO] Exiting data collecting mode...")
            print("[INFO] Closed")
            break
        elif key_events == ord('a'): 
            capture_drawing_status, key_option_colors = toggle_key_a(capture_drawing_status)
        elif key_events == ord('p'): key_p_on_click(model_path, [white_image], save_path)
        elif key_events == ord('c'): key_c_on_click()

        cv2.imshow("Predict mode", video_frame)
        cv2.imshow("white mode", white_image)

    cv2.destroyAllWindows() 