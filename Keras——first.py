#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tensorflow as tf
import keras 
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


# In[5]:


np.random.seed(123)


# In[6]:


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.utils import np_utils


# In[7]:


from keras.datasets import mnist# 载入数据集
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# In[8]:


print(X_train.shape, y_train.shape)


# In[9]:


from matplotlib import pyplot 


# In[10]:


X_train = X_train.reshape(X_train.shape[0], 28,28,1)
X_test = X_test.reshape(X_test.shape[0], 28,28,1)
print(X_train.shape)


# In[11]:


X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255


# In[12]:


print(y_train.shape)


# In[13]:


print(y_train[:10])


# In[14]:


# 将1维类数组转换为10维类矩阵
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
print(Y_train.shape)


# In[15]:


model = Sequential()


# In[16]:


model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))


# In[17]:


print(model.output_shape)


# In[18]:


model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.25))


# In[19]:


model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))


# In[20]:


model.compile(loss='categorical_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])


# In[21]:


model.fit(X_train, Y_train, batch_size=32, epochs=10, verbose=1)


# In[22]:


score = model.evaluate(X_test, Y_test, verbose=0)


# In[29]:


plt.imshow(X_train[0])


# In[33]:


c=model.save("G:/Users/MobileFile")


# In[27]:


img1=cv.imread("G:/Users/1.jpg")
img3=cv.imread("G:/Users/3.jpg")
img2=cv.imread("G:/Users/2.jpg")


# In[30]:


predict=model.predict(img1)


# In[31]:


#img1 =img1.reshape(None, 28,4)
#此处想要上传本地的数据，但是维数不对，且通过reshape修改不了图片的维数




# In[ ]:




