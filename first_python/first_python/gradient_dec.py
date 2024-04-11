# Here, given x and y values, we are trying to find m and b
# step: we start with a value of m and b, take baby steps to reach global minima as per 3D plane
# 3D plan axis: m, b, and MSE (Cost)

import numpy as numpy

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x) # we assume the lengths of x and y are similar
    learning_rate = 0.001

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        md = -(2/n)*sum(x*(y-y_predicted)) # partial derivate
        bd = -(2/n)*sum(y-y_predicted) # partial derivate
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, iteration {}".format(m_curr,b_curr,i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)