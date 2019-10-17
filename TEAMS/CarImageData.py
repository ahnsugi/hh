#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[3]:


# 1. 데이터 생성하기
train_datagen = ImageDataGenerator(rescale=1./255,
                                    rotation_range=10,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.7,
                                    zoom_range=[0.9,2.2],
                                    horizontal_flip=True,
                                    vertical_flip=True,
                                    fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
        'car_shape/train_image',
        target_size=(36,36),
        batch_size=3,
        class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'car_shape/test_image',
        target_size=(36,36),
        batch_size=3,
        class_mode='categorical')

# 2. 모델 구성하기
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3),
                    activation='relu',
                    input_shape=(36,36,3)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(5, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. 모델 학습시키기
model.fit_generator(
        train_generator,
        steps_per_epoch=30,
        epochs=100,
        validation_data=test_generator,
        validation_steps=5)

# 5. 모델 평가하기
print("-- Evaluate --")
scores = model.evaluate_generator(test_generator, steps=5)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 6. 모델 사용하기
print("-- Predict --")
output = model.predict_generator(test_generator, steps=5)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_generator.class_indices)
print(output)


# In[ ]:





# In[17]:


# 5. 모델 평가하기
print("-- Evaluate --")
scores = model.evaluate_generator(train_generator, steps=5)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))


# In[6]:


# Dropout 

from tensorflow.keras.layers import Dropout

# 1. 데이터 생성하기 
train_datagen = ImageDataGenerator(rescale=1./255,
                                    rotation_range=10,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.7,
                                    zoom_range=[0.9,2.2],
                                    horizontal_flip=True,
                                    vertical_flip=True,
                                    fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
        'car_shape/train_image',
        target_size=(36,36),
        batch_size=3,
        class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'car_shape/test_image',
        target_size=(36,36),
        batch_size=3,
        class_mode='categorical')

# 2. 모델 구성하기
model = Sequential()
model.add(Conv2D(32, (3,3), activation='elu', input_shape=(36,36,3)))
model.add(Conv2D(32, (3,3), activation='elu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation='elu'))
model.add(Conv2D(64, (3, 3), activation='elu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='elu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. 모델 학습시키기
model.fit_generator(
        train_generator,
        steps_per_epoch=300,
        epochs=200,
        validation_data=train_generator,
        validation_steps=5)

# 5. 모델 평가하기
print("-- Evaluate --")
scores = model.evaluate_generator(test_generator, steps=5)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 6. 모델 사용하기
print("-- Predict --")
output = model.predict_generator(test_generator, steps=5)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_generator.class_indices)
print(output)




# In[ ]:





# In[ ]:




