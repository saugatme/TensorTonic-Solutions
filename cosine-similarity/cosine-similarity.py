import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)
    x,y = 0,0

    if len(a) != len(b):
        raise ValueError
    else:
        dot_p = np.dot(a,b)
        for i in range(len(a)):
            x += a[i]**2
        xx = np.sqrt(x)
        
        for j in range(len(b)):
            y += b[j]**2
        yy = np.sqrt(y)
        if xx == 0 or yy == 0:
            return 0
        else:    
            sim = dot_p / (xx * yy)
        return sim
    pass