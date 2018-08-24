#!/usr/bin/env python
# -*- coding: utf-8 *

import numpy as np
import keras
from keras import backend as K
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
import json

# read config.json
def jsonReader():
    with open("./config.json", 'r') as load_f:
        jsonDict = json.load(load_f)
        return jsonDict

# read data from config.json
jsonData = jsonReader()
train_path = jsonData['train_path'] + '/train'
valid_path = jsonData['train_path'] + '/valid'
test_path = jsonData['train_path'] + '/test'
bsize = int(jsonData['batch_size_train'])
catnum = int(jsonData['category_num'])
lrate = float(jsonData['learning_rate'])
steps = int(jsonData['steps_per_epoch'])
epoch_num = int(jsonData['epoch_num'])
output_name = jsonData['output_name']


train_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(
    train_path, target_size=(224,224), batch_size=bsize)
valid_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(
    valid_path, target_size=(224,224), batch_size=10)
test_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(
    test_path, target_size=(224,224), batch_size=2, shuffle=False)

mobile = keras.applications.mobilenet.MobileNet()


x = mobile.layers[-6].output
predictions = Dense(catnum, activation='softmax')(x)
model = Model(inputs=mobile.input, outputs=predictions)

model.summary()

for layer in model.layers[:-5]:
    layer.trainable = False
model.compile(Adam(lr=lrate), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit_generator(train_batches, steps_per_epoch=steps, 
                    validation_data=valid_batches, validation_steps=2, epochs=epoch_num, verbose=2)

model.save(output_name)

predictions = model.predict_generator(test_batches,steps=1, verbose=2)
print(predictions)
print(train_batches.class_indices)







