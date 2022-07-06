import numpy as np
import matplotlib.pyplot as plt

from math import *

def rbf (x_basis, x, eps):
    """
    Returns the result of the radial basis function with a squared epsilon. 
    Takes the centre x_basis, the independent value x and a value for epsilon as eps.
    """
    return exp(- ((np.linalg.norm(x_basis - x))**2) / (eps**2))

def nonlin_decomp (x, x0, L, C, eps):
    """
    Performs the nonlinear decomposition with the radial basis function. 
    Takes the independent value x, the matrix X, the number of summands L, the coefficient matrix C and epsilon as eps.
    """
    sum = 0
    for i in range(L):
        sum += C[:, i]*rbf(x0[:, i], x, eps)
    return sum