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
    def __init__(self, bodies):
        self.bodies = np.array(bodies)
        
        for body in self.bodies:
            body.position = np.array([body.position[0], body.position[1]])
            
        
    def compute_force_vectors(self):
        distance_list = []
        force_list = []
        net_force = []
        
        for primary_body in self.bodies:
            temp = []
            for secondary_body in self.bodies:
                distance = secondary_body.position - primary_body.position
                temp.append(distance)
            distance_list.append(temp)
        distance_list = np.array(distance_list)
            
        
        
        for i, primary_body in enumerate(self.bodies):
            temp = []
            for j, secondary_body in enumerate(self.bodies):
                force = 6.67e-11 * primary_body.mass * secondary_body.mass / magnitude(distance_list[i,j])
                force = force * unit_vector(distance_list[i,j])
                temp.append(force)
            force_list.append(temp)
        force_list = np.array(force_list)
    

        for obj in force_list:
            net_force.append(obj.sum(axis=0))
            
        return net_force