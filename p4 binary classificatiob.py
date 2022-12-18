from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
dataset=loadtxt('diabetes.csv',delimiter=',')
print(dataset)
X=dataset[:,0:8]
Y=dataset[:,8]
model=Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X,Y,epochs=150,batch_size=10)
prediction =model.predict_step(X)





