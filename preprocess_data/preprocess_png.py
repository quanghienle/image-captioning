import cv2
import glob
import numpy as np
import pickle
from tensorflow.keras.applications import ResNet50

def get_name_from_file(file_name):
    """ get file names from path
        file names here are just numbers that match the png with svg file
    """
    file_number = file_name.split('/')[-1].split('.')[0]
    return int(file_number)


def get_img_arr(png_path):
    png_images = glob.glob(F'{png_path}/*.png')
    png_arr = [None] * len(png_images)
    for i in png_images:
        png_arr[get_name_from_file(i)] = cv2.imread(i)

    return np.array(png_arr)

def encode_and_save_images(png_path, dest_path):
    png_data = get_img_arr(png_path)
    print(png_data.shape)
    resnet = ResNet50(include_top=False,weights='imagenet',input_shape=(100,100,3),pooling='avg')
    #  print(resnet.summary())

    print('Extracting features from images...')
    encoded_images = resnet.predict(png_data, verbose=1) 
    print(f'Encoded images shape: {encoded_images.shape}')

    print('Saving extracted features to dataset/preprocessed_data/X.pkl')
    with open(f'{dest_path}/X.pkl','wb') as f:
        pickle.dump(encoded_images, f)

    print('DONE')




