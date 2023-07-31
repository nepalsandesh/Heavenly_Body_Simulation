import numpy as np


def magnitude(arr):
    """Returns the magnitide of the vector.
    """
    return np.sqrt(arr[0]**2 + arr[1]**2 + arr[2]**2)

def unit_vector(arr):
    """Computes and returns unit vector."""
    mag = magnitude(arr=arr)
    return arr/mag



class PhysicsEngine:
    def __init__(self):
        pass