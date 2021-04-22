from search.src import getData
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, Conv1D, Flatten
from keras import regularizers
''',kernel_regularizer = regularizers.l2(regularValue)'''
def getModel(numHidden, numNeuron, hasBatch=False, rate=0, regularValue=0, epochs=20, activationFunction='relu'):
    model = Sequential()
    for i in range(numHidden):
        if i == 0:
            if regularValue > 0:
                model.add(Dense(numNeuron, activation = activationFunction, input_shape = (len(
                    getData.championIxDict),), kernel_regularizer = regularizers.l2(regularValue)))
            else:
                model.add(Dense(numNeuron, activation = activationFunction, input_shape = (len(
                    getData.championIxDict),)))
        else:
            if regularValue > 0:
                model.add(Dense(numNeuron, activation = activationFunction,kernel_regularizer = regularizers.l2(regularValue)))
            else:
                model.add(Dense(numNeuron, activation = activationFunction))
        if hasBatch:
            model.add(BatchNormalization())
        if rate > 0:
            model.add(Dropout(rate))
    
    
    model.add(Dense(1, activation = 'sigmoid',  kernel_initializer = "he_normal"))
    model.compile(optimizer = 'rmsprop',loss = 'binary_crossentropy',metrics=['accuracy'])
    
    return model

def getModel2():
    model = Sequential()
    
    model.add(Conv1D(3, 4, padding = 'same', activation = 'relu', input_shape = (1,len(getData.championIxDict))))
    model.add(BatchNormalization())
    model.add(Conv1D(3,8,padding = 'same',activation = 'relu'))
    model.add(BatchNormalization())
    model.add(Conv1D(3,16,padding = 'same',activation = 'relu'))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dense(16,activation = 'relu'))
    
    model.add(Dense(1, activation = 'sigmoid',  kernel_initializer = "he_normal"))
    model.compile(optimizer = 'rmsprop',loss = 'binary_crossentropy',metrics=['accuracy'])
    return model