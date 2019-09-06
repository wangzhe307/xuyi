import numpy as np
from skimage.external import tifffile as tiff
import cv2
import random
from keras.utils import np_utils
class Config:
    img_rows = 256
    img_cols = 256
    num_channels = 5
    num_mask_channels = 12

def flip_axis(x, axis):
    x = np.asarray(x).swapaxes(axis, 0)
    x = x[::-1, ...]
    x = x.swapaxes(0, axis)
    return x

def form_batch(X, y, batch_size):
    X_batch = np.zeros((batch_size, Config.img_rows, Config.img_cols,Config.num_channels))
    y_batch = np.zeros((batch_size, Config.img_rows, Config.img_cols,Config.num_mask_channels))
    X_height = X.shape[1]
    X_width = X.shape[2]
    for i in range(batch_size):
        random_width = random.randint(0, X_width - Config.img_cols - 1)
        random_height = random.randint(0, X_height - Config.img_rows - 1)
        random_image = random.randint(0, X.shape[0] - 1)
        y_batch[i] = y[random_image, random_height: random_height + Config.img_rows, random_width: random_width + Config.img_cols,:]
        X_batch[i] = np.array(X[random_image,random_height: random_height + Config.img_rows, random_width: random_width + Config.img_cols,:])
    return X_batch, y_batch

def batch_generator(X, y, batch_size, horizontal_flip=False, vertical_flip=False, swap_axis=False):
    while True:
        X_batch, y_batch = form_batch(X, y, batch_size)
        for i in range(X_batch.shape[0]):
            xb = X_batch[i]
            yb = y_batch[i]

            if horizontal_flip:
                if np.random.random() < 0.5:
                    xb = flip_axis(xb, 1)
                    yb = flip_axis(yb, 1)

            if vertical_flip:
                if np.random.random() < 0.5:
                    xb = flip_axis(xb, 2)
                    yb = flip_axis(yb, 2)

            if swap_axis:
                if np.random.random() < 0.5:
                    xb = xb.swapaxes(1, 2)
                    yb = yb.swapaxes(1, 2)

            X_batch[i] = xb
            y_batch[i] = yb


        yield ([X_batch,X_batch,X_batch],y_batch)

def getTrainDataAndMask(tifPath,maskPath):
    data = np.expand_dims(tiff.imread(tifPath),0)
    mask = np.expand_dims(np_utils.to_categorical(cv2.imread(maskPath,0),12),0)
    return data/255,mask

