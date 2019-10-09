import math
import numpy as np


def sigmoid(x):
    return 2 /(1 + np.exp(-x)) - 1

def sigmoid_dot(x):
    return (1 - sigmoid(x)**2) / 2

def matrixsig(A):
    return np.sum(sigmoid(A)), np.sum(sigmoid_dot(A))

A = np.array([[1, 0, np.sin(np.pi/4)],[0, 1, np.sin(np.pi/2)],[1, 0, 1]])


print(matrixsig(A))

