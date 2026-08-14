import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    # Write code here
    if len(x) != len(y):
        raise ValueError
    if len(x) == len(y):
        res = 0 
        for c in range(len(x)):
            res += x[c] * y[c]
    return float(res)