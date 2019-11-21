'''
Name: Jael Butler
Class: CS 4820
Duedate: 10/ /2019

This module contains the code for the Deep Cube.
Referenced: https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
            to learn how to use Keras.
'''
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

sizes = [2]


for n in sizes:
    print("\nTesting size", n, "\n")

    # Get training data.
    training_set = np.genfromtxt('./datasets/training/size'+str(n)+'.csv', delimiter=',')
    x_train, y_train = np.hsplit(training_set, np.array([-1]))
    y_train = to_categorical(y_train)
    input_size = len(x_train[0])
    #print(x_train, y_train)

    # Define DNN model
    model = Sequential()
    model.add(Dense(input_size // 2, input_dim=input_size, activation='relu'))       # Hidden layer 1.
    model.add(Dense(31, activation='sigmoid'))                                       # Output layer.
    
    # Compile DNN.
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the DNN
    model.fit(x_train, y_train, epochs=10, batch_size=1000)

    # Test DNN
    testing_set = np.genfromtxt('./datasets/testing/size'+str(n)+'.csv', delimiter=',')
    x_test, y_test = np.hsplit(testing_set, np.array([-1]))
    y_test = to_categorical(y_test)
    _, accuracy = model.evaluate(x_test, y_test)
    print(accuracy*100, "%")

    