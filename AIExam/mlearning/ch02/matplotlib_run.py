'''
Created on Jan 25, 2018

@author: I302783
'''
from matplotlib import pyplot
from numpy import *

x = arange(1, 10)
y = x
fig = pyplot.figure()
ax1 = fig.add_subplot(111)
# set title
ax1.set_title('Scatter Plot')
pyplot.xlabel('X')
pyplot.ylabel('Y')
# scatter figure
ax1.scatter(x, y, c=['r', 'g', 'b'], marker='o')
# set img
pyplot.legend('x1')
pyplot.show()
