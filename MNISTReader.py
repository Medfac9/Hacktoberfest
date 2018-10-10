"""
Autor: Alejandro Guerrero Martínez

Lector de datos MNIST en python modificado
a partir del archivo obtenido en https://gist.github.com/akesling/5358964
bajo licencia GPL.

Modificaciones propias:
- Modificado para funcionar en Python3.6
- Eliminada funcionalidad innecesaria
- Modificada función de lectura para devolver los dos arrays numpy
- Adaptados los arrays para funcionar en Keras
"""

import os
import struct
import numpy as np
from keras.utils import np_utils

def read(dataset = "training", path = "."):

    num_outputs = 10
    img_channels = 1

    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)
        #Formateo de las etiquetas para su uso con keras
        lbl = np_utils.to_categorical(lbl, num_outputs)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(num, img_channels, rows, cols)
        #Normalización de los datos del vector de imágenes
        img = img.astype('float32')
        img /= 255

    return lbl,img
