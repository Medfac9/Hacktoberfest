"""

Autor: Alejandro Guerrero Martínez

Resolución del problema MNIST con una tasa de error aproximada de 0.60 % (Depende de cada ejecución)
Uso de Keras con TensorFlow como backend.

Keras - https://keras.io/
TensorFlow - https://www.tensorflow.org/

"""

import MNISTReader as datareader
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# Lectura de los datos de MNIST
training_labels, training_images = datareader.read(dataset='training', path='./MNIST-Data')
testing_labels, testing_images = datareader.read(dataset='testing', path='./MNIST-Data')

input_shape=(1,28,28)


"""
# Red Neuronal con Keras
"""

from keras import backend as K
from keras import regularizers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, PReLU, Conv2D, Flatten, MaxPooling2D, AveragePooling2D
from time import time

#Especifica el formato de dato de las imágenes
K.set_image_dim_ordering('th')

#Topología de la Red neuronal
model = Sequential()


#Capa Convulacional con 64 neuronas, máscara de 6x6 y activación PReLU
model.add(Conv2D(64, (6, 6), activation='linear', input_shape=input_shape))
model.add(PReLU())

#Capa Convulacional con 128 neuronas, máscara de 4x4, Averagepooling, dropout del 25% y activación PReLU
model.add(Conv2D(128, (4, 4), activation='linear'))
model.add(PReLU())
model.add(AveragePooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

#Capa de "aplanado"
model.add(Flatten())

#Capa Dense con 256 neuronas, dropout del 20% y activación PReLU
model.add(Dense(256, activation='linear'))
model.add(PReLU())
model.add(Dropout(0.2))

#Capa Dense con 256 neuronas, dropout del 20% y activación PReLU
model.add(Dense(256, activation='linear'))
model.add(PReLU())
model.add(Dropout(0.2))

#Capa Dense de salida softmax (10 salidas)
model.add(Dense(units=10, activation='softmax'))



#Crea la red neuronal con la opción de optimización
model.compile(loss='categorical_crossentropy', optimizer='adagrad', metrics=['accuracy'])

#Obtiene el tiempo de inicio
inittime = time()

#Entrena la red neuronal
training = model.fit(training_images, training_labels,
          epochs=20, batch_size=128, verbose=2,
          validation_data=(testing_images, testing_labels))

#Obtiene el tiempo de entrenamiento
training_time = time()-inittime

print ("\nTiempo de entrenamiento: ", training_time)

#Obtiene el porcentaje de error

evaluation = model.evaluate(testing_images, testing_labels, verbose=2)

print("Porcentaje de error sobre Conjunto de Prueba: ", (1 - evaluation[1])*100)

#Obtenemos una gráfica sobre la precisión en cada época
fig = plt.figure()
plt.subplot(2,1,1)
plt.plot(training.history['acc'])
plt.plot(training.history['val_acc'])
plt.title('Red Neuronal')
plt.ylabel('precisión')
plt.xlabel('épocas')
plt.legend(['entrenamiento', 'prueba'], loc='lower right')
plt.tight_layout()
fig.savefig("EntrenamientoRedNeuronal.png")

#Obtiene los resultados sobre el conjunto de prueba
predicted_classes = model.predict_classes(testing_images)

print("Vector de Resultados:")
np.set_printoptions(threshold=np.nan)
print(np.array2string(predicted_classes, separator=''))

exit()
