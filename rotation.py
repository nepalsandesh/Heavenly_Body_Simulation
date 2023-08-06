import numpy as np



def rotate_x(positions, theta):
    rotation_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    positions = np.array(positions)
    rotated_position = np.dot(rotation_x, positions)
    print("rotated_position : \n" ,rotated_position)
    return rotated_position