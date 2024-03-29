# -*- coding: utf-8 -*-
"""CurveFitting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oQqE2Tvwf0J5E26-upDnwfNVJmkOWiF5

# Non linear regression / curve fitting
"""

3+2

!pwd

#imports
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import tensorflow as tf
import math
import csv
import glob
from PIL import Image
import re

print ('TensorFlow version: ' + tf.__version__)

#loading data
norm_list = []
prob_list = []

with open('NORM.csv', 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            norm_list.append(row[0])

with open('PROB.csv', 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            prob_list.append(row[0])

norm_list, prob_list = (list(t) for t in zip(*sorted(zip(norm_list, prob_list))))

x_data = np.array(norm_list)
y_data = np.array(prob_list)
x_data = x_data.astype(np.float)
y_data = y_data.astype(np.float)

# Display the dataset
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.scatter(x_data[::1], y_data[::1], s=1)
plt.grid()
plt.xlabel('Normalized symtopm score')
plt.ylabel('Lyme probability')
plt.title("Probability from KDE")
plt.show()
# plt.savefig('orgdata.png',dpi=300)
# files.download('orgdata.png')

#Model Creation
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units = 1, activation = 'linear', input_shape=[1]))
model.add(tf.keras.layers.Dense(units = 64, activation = 'relu'))
model.add(tf.keras.layers.Dense(units = 64, activation = 'relu'))
model.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))
model.compile(loss='mse', optimizer="adam")

# Display model summary
model.summary()

!pwd

# Training
model.fit( x_data, y_data, epochs=100, verbose=1)
model.save('Qmodel.h5') #Save model for later

#Callbacks
# METRICS = [keras.metrics.BinaryAccuracy(name='accuracy')]
# base_learning_rate = 0.0001
# model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
#           loss=tf.keras.losses.BinaryCrossentropy(),
#           metrics=METRICS)
# early_stopping = EarlyStopping(monitor='val_accuracy', patience=10, verbose=1, restore_best_weights=True)
# reduce_lr = ReduceLROnPlateau(monitor='val_accuracy', patience=5, verbose=1)
# csv_logger = CSVLogger(os.path.join(MODEL_SAVE_DIRECTORY,"model_history_log_fold"+str(i)+".csv"), append=True)
# history_bef_finetune = model.fit(train_dataset, epochs=MAX_EPOCH, validation_data=validation_dataset, callbacks=[early_stopping, reduce_lr, csv_logger])

# Compute the output
y_predicted = model.predict(x_data)

# Display the result
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.scatter(x_data[::1], y_data[::1], s=1)
plt.scatter(x_data[::1], y_predicted[::1], s=1)
plt.xlabel('Normalized symtopm score')
plt.ylabel('Lyme probability')
plt.title("Neural Curve fitting")
plt.grid()
plt.show()
# plt.savefig('training.png', dpi=300)
# files.download("training.png")

#predict on arbitraty data
norm_score=0.9
y_predicted = model.predict([norm_score])
print(y_predicted)

#Create GIF of the training performance
# Create the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units = 1, activation = 'linear', input_shape=[1]))
model.add(tf.keras.layers.Dense(units = 64, activation = 'relu'))
model.add(tf.keras.layers.Dense(units = 64, activation = 'relu'))
model.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))
model.compile(loss='mse', optimizer="adam")

for x in range(100):
  # One epoch
  model.fit( x_data, y_data, epochs=1, verbose=1)

  # Compute the output
  y_predicted = model.predict(x_data)

  # Display the result
  plt.scatter(x_data[::1], y_data[::1], s=1)
  plt.scatter(x_data[::1], y_predicted[::1], s=1)
  plt.grid()
  plt.xlim(0, 1)
  plt.ylim(0, 1)
  plt.xlabel('Normalized symtopm score')
  plt.ylabel('Lyme probability')

  # displaying the title
  plt.title("Neural Curve fitting Epoch: "+str(x))
  #plt.show()
  plt.savefig('/content/training4/'+ str(x) ,dpi=300)
  # files.download('training-' + str(x) +'-epochs.png')
  plt.clf()

# filepaths
fp_in = "/content/training4/*.png"
fp_out = "curve_fitting_sig.gif"

natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)]

# # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in), key=natsort)]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)

natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)]

r=natsort("10.png")
r

r=natsort("2.png")
r

import re

r = re.split("!","!Hello!World")
r

"!".join(['Hello', 'World'])

a,*b = [1,2,3,4]
print(a,b)

