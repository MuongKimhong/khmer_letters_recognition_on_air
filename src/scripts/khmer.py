from utils import ImageProcessing

path = '/Users/muongkimhong/Developments/khmer_letters_recognition_on_air/src/scripts/dataset/3/'
ImageProcessing().resize_images_in_dir(dir_path=path, new_width=128, new_height=128)