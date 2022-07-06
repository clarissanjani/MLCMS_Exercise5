import numpy as np
import matplotlib.pyplot as plt

from math import *



def readData(fileName):
    """
    Takes the path of a text file that contains 2d data, separated by a blank space.
    Returns the data in a numpy array with two columns.
    """
    
    array = [[], []]
    
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
        
    for line in lines:
        elements = line.split(' ')
        array[0].append(elements[0])
        array[1].append(elements[1])
        
    return np.array(array, dtype = "float64")

def rbf (x_basis, x, eps):
    """
    Returns the result of the radial basis function with a squared epsilon. 
    Takes the centre x_basis, the independent value x and a value for epsilon as eps.
    """
    return exp(- ((x_basis - x)**2) / (eps**2))

def nonlin_decomp (x, X, L, C, eps):
    """
    Performs the nonlinear decomposition with the radial basis function. 
    Takes the independent value x, the matrix X, the number of summands L, the coefficient matrix C and epsilon as eps.
    """
    sum = 0
    for i in range(L):
        sum += C[i]*rbf(X[i], x, eps)
    return sum

def calc_PHI (X, L, eps):
    """
    Calculates and returns the matrix PHI. Takes the initial data vector X, the number of summands L and epsilon as eps.
    """

    PHI = np.zeros([1000, L])

    for i in range(1000):
        for j in range(L):
            PHI[i, j] = rbf(X[i], X[j], eps)
            
    return PHI


def calc_C (PHI, F):
    """
    Calculates and returns the matrix C. Takes the PHI and the intial solutions vector C.
    """
    
    return (np.linalg.inv((PHI.transpose()@PHI))@PHI.transpose()@F).transpose()


def calc_error (F, results_array):
    """
    Calculates and returns the error with the numpy function numpy.linalg.norm(). Takes two arrays of the same dimension. 
    """

    error_array = F - results_array

    return np.linalg.norm(error_array)

    