import numpy as np

def custom_projection_matrix(distance, rotated_points):
    z = 1 / (distance - rotated_points[:, 2])
    
    projected_points = rotated_points[:, :2] * z[:, np.newaxis]
    
    return projected_points

# Example usage
distance = 500.0  # Distance from the camera
rotated_points = np.array([
    [82.25643614, -43.31653236, 266.40499178],
    [-89.55211514, 499.26493091, -92.39224651],
    # ... (other points)
])

projected_points = custom_projection_matrix(distance, rotated_points)
print("Projected Points:\n", projected_points)
