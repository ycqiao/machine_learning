'''
Created on Jan 26, 2018

@author: I302783
'''
from kNN import *
from os import listdir


def image2Vector(filename):
    returnVector = zeros((1, 1024))
    fileReader = open(filename)
    for i in range(32):
        lineStr = fileReader.readline()
        for j in range(32):
            returnVector[0, 32 * i + j] = int(lineStr[j])
    return returnVector


def handleWritingClassTest():
    from __builtin__ import int
    from __builtin__ import float
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    numTrainingFiles = len(trainingFileList)
    trainingMatrix = zeros((numTrainingFiles, 1024))
    for i in range(numTrainingFiles):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        savedNum = int(fileStr.split('_')[0])
        hwLabels.append(savedNum)
        trainingMatrix[i, :] = image2Vector('trainingDigits/%s' % fileNameStr)

    testFileList = listdir('testDigits')
    errorCount = 0.0
    numTests = len(testFileList)
    for i in range(numTests):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        savedNum = int(fileStr.split('_')[0])
        vectorUnderTest = image2Vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMatrix, hwLabels, 3)
        print 'the classifier came back with: %d, the real answer is: %d' % (classifierResult, savedNum)
        if (classifierResult != savedNum):
            errorCount += 1.0
    print('\nthe total number of tests: %d, the total number of errors: %d\n' % (numTests, errorCount))
    print('\nthe total error rate is: %s' % (errorCount / float(numTests)))

handleWritingClassTest()
