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

# run matplotlib
import numpy as np
from numpy import array
import  matplotlib
import matplotlib.pyplot as pyplot

fig = pyplot.figure()
ax = fig.add_subplot(111)
# ax.scatter(datingMat[:,1], datingMat[:,2])
ax.scatter(datingMat[:, 1], datingMat[:, 2], s=60, marker='*', c=['r', 'g', 'b', 'y'])
# ax.scatter(datingMat[:,1], datingLabels)
pyplot.show()

# import numpy as np
#
# x = np.arange(0, 5, 0.1);
# y = np.sin(x)
# bx = fig.add_subplot(111)
# bx.plot(x, y)
# pyplot.show()
