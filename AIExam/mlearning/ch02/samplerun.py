'''
Created on Jan 25, 2018

@author: I302783
'''
import kNN

group, labels = kNN.createDataset()

print group, labels

datingMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
print datingMat[:4]
print datingLabels[:4]

from numpy import array
import  matplotlib
import matplotlib.pyplot as pyplot


def pyplotTest():
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(datingMat[:,1], datingMat[:,2])
    ax.scatter(datingMat[:, 1], datingMat[:, 2], s=60, marker='*', c=['r', 'g', 'b', 'y'])
    # ax.scatter(datingMat[:,1], datingLabels)
    pyplot.show()


import numpy as np


def pyplotTest2():
    fig = pyplot.figure()
    x = np.arange(0, 5, 0.1);
    y = np.sin(x)
    bx = fig.add_subplot(111)
    bx.plot(x, y)
    pyplot.show()


def autoNormTest():
    normMat, ranges, minVals = kNN.autoNorm(datingMat)
    print normMat
    print ranges
    print minVals


def datingClassTest():
    hoRatio = 0.550
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = kNN.classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print 'the classifier came back with: %s, the real answer is: %s' % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))


datingClassTest()

kNN.classifyPerson()