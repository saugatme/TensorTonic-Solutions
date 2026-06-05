import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    ans = 1 / (1 + np.exp(-1*np.array(x)))
    return ans