'''
Created on Jan 25, 2018

@author: I302783
'''
import operator

from numpy import *


def createDataset():
    group = array([[1.0, 1, 1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataset, labels, k):
    datasetSize = dataset.shape[0]
    diffMat = tile(inX, (datasetSize, 1)) - dataset
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    lines = fr.readlines()
    numLines = len(lines)
    returnMat = zeros((numLines, 3))
    labels = []
    index = 0
    for line in lines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        labels.append(listFromLine[-1])
        index += 1
    return returnMat, labels


def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals
    normDataset = zeros(shape(dataset))
    numRows = normDataset.shape[0]
    normDataset = dataset - tile(minVals, (numRows, 1))
    normDataset = normDataset / tile(ranges, (numRows, 1))
    return normDataset, ranges, minVals

def classifyPerson():
    resultSet = ['not at all', 'in small doess', 'in large doses']
    
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input('frequent filer miles earned per year?'))
    iceCream = float(raw_input('liters of ice cream consumed per year?'))
    
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)    
    inArr = array([ffMiles, percentTats, iceCream])
    
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print "You will probably like this person: ", resultSet[int(classifierResult) - 1]
