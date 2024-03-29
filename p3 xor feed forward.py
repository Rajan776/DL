#solving xor problem using deep feed forward network

import numpy as np
from keras.layers import  Dense
from keras.models import  Sequential
model=Sequential()
model.add(Dense(units=2,activation='rele',input_dim=2))
model.add(Dense(units=1,activation='sigmoidal'))
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
print(model.summary())
print(model.get_weights())
x=np.array([[0.,0.],[0.,1.],[1.,1.]])
y=np.array([[0.],[1.],[1.],[0.]])
model.fit(x,y,epochs=1000,batch_size=4)
print("final weight=")
print(model.get_weights())
print(model.predict(x,batch_size=4))

