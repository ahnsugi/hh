#!/usr/bin/env python
# coding: utf-8

# ### tensorflow 설치

# In[1]:


get_ipython().system('pip install tensorflow==2.0.0-alpha0')


# In[1]:


import tensorflow as tf
print(tf.__version__)


# In[9]:


import tensorflow as tf
print(tf.__version__)
import tensorflow.keras.utils as utils
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import numpy as np


# In[10]:


# 1. 데이터셋 준비하기 / X는 입력 훈련데이터, Y=2x , val은 validation검증데이터
X_train = np.array(
[
    1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
]
)

Y_train = np.array(
[
    2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18
])

X_val = np.array(
[
    1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
])

Y_val = np.array(
[
    2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18,2,4,6,8,10,12,14,16,18
])


# In[11]:


print(X_train.shape)
print(X_train)
print(Y_train.shape)
print(Y_train)


# In[12]:


# 라벨링 전환 / 확률로 리턴하도록 정답을 분류하다.
Y_train = utils.to_categorical(Y_train,19)
Y_val = utils.to_categorical(Y_val,19)


# In[13]:


print(X_train)
print(Y_train)
print(Y_train.shape)
print(Y_val)
print(Y_val.shape)


# In[14]:


model = Sequential() #dense는 멀티레이어 층, activation는 흐른다 흐르지않는다를 각각 다른 특징으로 신호를 준다.
model.add(Dense(units=38, input_dim=1, activation='elu'))
model.add(Dense(units=19,  activation='softmax'))


# In[21]:


# 3. 모델 엮기
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 4. 모델 학습시키기 / verbose 0일때(없고)와 1일때,2 일때 학습 결과를 더 상세하게 보여주는 역할, batch_size는 한번에 몇 문제를 풀것인가,
hist = model.fit(X_train, Y_train, epochs=200, batch_size=1, verbose=1, validation_data=(X_val, Y_val))


# In[22]:


# 5. 모델 학습 과정 표시하기 epoch는 몇 번 반복했는지, 학습한 결과를 보여주고 있다.
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()


# In[20]:


# 6. 모델 사용하기
X_test = np.array([
    1,2,3,4,5,6,7,8,9
])
Y_test = np.array([
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    
])
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=1)

print('')
print('loss : ' + str(loss_and_metrics[0]))
print('accuray : ' + str(loss_and_metrics[1]))


# ### 28 * 28 숫자 인식

# In[141]:


width = 28
height = 28
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, width*height).astype('float32') / 255.0 # reshape는 가로28 * 세로28 을 한줄로 나타내기 위해서, 정규화 위해서 255로 나눈다.
x_test = x_test.reshape(10000, width*height).astype('float32') / 255.0


# In[142]:


x_val = x_train[50000:] # 50000개는 훈련 데이터로 사용하겠다.
y_val = y_train[50000:]
x_train = x_train[:50000]
y_train = y_train[:50000]


# In[ ]:





# In[143]:


y_train = utils.to_categorical(y_train)
y_val = utils.to_categorical(y_val)
y_test = utils.to_categorical(y_test)


# In[144]:


model = Sequential() #dense는 멀티레이어 층, activation는 흐른다 흐르지않는다를 각각 다른 특징으로 신호를 준다.
model.add(Dense(units=10, input_dim=784, activation='elu'))
model.add(Dense(units=10,  activation='softmax'))


# In[145]:


# 3. 모델 엮기
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 4. 모델 학습시키기 / verbose 0일때(없고)와 1일때,2 일때 학습 결과를 더 상세하게 보여주는 역할, batch_size는 한번에 몇 문제를 풀것인가,
hist = model.fit(x_train, y_train, epochs=20, batch_size=10, verbose=1, validation_data=(x_val, y_val))


# In[ ]:





# In[ ]:




