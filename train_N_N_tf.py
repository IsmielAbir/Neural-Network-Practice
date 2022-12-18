# Train Neural Network using Tensorflow 
# epochs number of gradient descent 


import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.losses import BinaryCrossentropy

model = Sequential([
    Dense(units=25, activation='sigmoid'),
    Dense(units=15, activation='sigmoid'),
    Dense(units=1, activation='sigmoid')

])

model.compile(loss=BinaryCrossentropy())
model.fit(X,y,epochs=100)

