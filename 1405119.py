import numpy as np
import math
import random


def sigmoid(x):
    return 1/(1+math.exp(-x))


layerDimensions = [3, 4]
featureNo = 0
labelNo = 4

featureTrainList = []
labelTrain = []
labelTrainList = []
weightVectorList = []
neuronLayer = []

featureTestList = []
labelTest = []


def readTrain():
    file = open("trainNN.txt", "r")
    trainDataSize = -1
    while True:
        trainDataSize += 1
        featureTrain = []
        data = file.readline()
        if data == "":
            break
        datanow = data.split()
        featureNo = len(datanow) - 1
        for i in range(0, featureNo):
            featureTrain.append(float(datanow[i]))
        featureTrain.append(1.0)
        featureTrainList.append(featureTrain[:])
        labelTrain.append(int(datanow[featureNo]))
    labelNo = len(set(labelTrain))
    for i in range(0, trainDataSize):
        trainVector = []
        for j in range(0, labelNo):
            trainVector.append(0)
        trainVector[labelTrain[i] - 1] = 1
        labelTrainList.append(trainVector)


def initWeight(layerNo):
    d = layerDimensions[layerNo]
    for j in range(0, labelNo+1):
        weightVector = []
        for i in range(0, d):
            weightVector.append(float(np.random.uniform(0, 1, 1)))
        weightVectorList.append(weightVector)


def forward():
    for i in range(0, len(layerDimensions)):
        initWeight(i)
        #print(featureTrainList)
        #print(weightVectorList)
        #print(np.matmul(np.matrix(featureTrainList), np.matrix(weightVectorList)))
        #print(a)


def readTest():
    file = open("testNN.txt", "r")

    while True:
        featureTest = []
        data = file.readline()
        if data == "":
            break
        datanow = data.split()
        featureNo = len(datanow) - 1
        for i in range(0, featureNo):
            featureTest.append(datanow[i])
        featureTestList.append(featureTest[:])
        labelTest.append(datanow[featureNo])


def main():
    readTrain()
    forward()


main()