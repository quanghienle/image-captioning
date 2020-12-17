import cv2
import glob
import numpy as np
import pickle
from tensorflow.keras.applications import ResNet50

import utils as utils


def get_img_arr():
    png_images = glob.glob('../dataset/png_data/*.png')
    png_arr = [None] * len(png_images)
    for i in png_images:
        png_arr[utils.get_name_from_file(i)] = cv2.imread(i)

    return np.array(png_arr)

def encode_and_save_images():
    png_data = get_img_arr()
    resnet = ResNet50(include_top=False,weights='imagenet',input_shape=(100,100,3),pooling='avg')
    #  print(resnet.summary())

    print('Extracting features from images...')
    encoded_images = resnet.predict(png_data, verbose=1) 
    print(f'Encoded images shape: {encoded_images.shape}')

    print('Saving extracted features to dataset/preprocessed_data/X.pkl')
    with open('../dataset/preprocessed_data/X.pkl','wb') as f:
        pickle.dump(encoded_images, f)

    print('DONE')




