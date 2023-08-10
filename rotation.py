import numpy as np


# projection_matrix = np.array([
#     [1, 0, 0]
# ])



def rotate_x(positions, theta):
    print(positions.shape)
    positions = positions.reshape((-1,1))
    # print("position.shape \,", positions.shape)
    rotation_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    rotated_position = np.dot(rotation_x, positions)
    # print("rotated_position : \n" ,rotated_position)
    return rotated_position.reshape(3)


def rotate_y(positions, theta):
    positions = positions.reshape((-1,1))
    # print("position.shape \,", positions.shape)
    rotation_y = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])
    rotated_position = np.dot(rotation_y, positions)
    return rotated_position.reshape(3)


def rotate_z(positions, theta):
    positions = positions.reshape((-1,1))
    # print("position.shape \,", positions.shape)
    rotation_z = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    rotated_position = np.dot(rotation_z, positions)
    return rotated_position.reshape(3)


def get_rotated_orbit(coordinates, direction, angle):
    temp = []
    if direction == "x":
        for point in coordinates:
            rotated_point = rotate_x(np.array(point), angle)
            temp.append(rotated_point)
        return temp
    if direction == "y":
        for point in coordinates:
            rotated_point = rotate_x(np.array(point), angle)
            temp.append(rotated_point)
        return temp
    if direction == "z":
        for point in coordinates:
            rotated_point = rotate_x(np.array(point), angle)
            temp.append(rotated_point)
        return temp
    else:
        return coordinates
    
        
        
            
        