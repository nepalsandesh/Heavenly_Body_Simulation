import numpy as np

# def custom_projection_matrix(distance, rotated_points):
#     z = 1 / (distance - rotated_points[:, 2])
    
#     projected_points = rotated_points[:, :2] * z[:, np.newaxis]
    
#     return projected_points

# # Example usage
# distance = 500.0  # Distance from the camera
# rotated_points = np.array([
#     [82.25643614, -43.31653236, 266.40499178],
#     [-89.55211514, 499.26493091, -92.39224651],
#     # ... (other points)
# ])

# projected_points = custom_projection_matrix(distance, rotated_points)
# print("Projected Points:\n", projected_points)



# --------------------------------------------------------------vectorized operations--------------------
# import numpy as np

# class Body:
#     def __init__(self, position, mass, radius):
#         self.position = position
#         self.mass = mass
#         self.radius = radius

# # Create instances of the Body class
# b1 = Body(np.array([0, 0]), 10, 1)
# b2 = Body(np.array([1, 1]), 15, 1)
# b3 = Body(np.array([2, 2]), 20, 1)
# b4 = Body(np.array([3, 3]), 25, 1)

# # Create an array of instances
# body_array = np.array([b1, b2, b3, b4])

# # New mass values
# new_mass_values = np.array([30, 35, 40, 45])

# # Update mass values using a list comprehension and setattr
# [setattr(body_array[i], 'mass', new_mass) for i, new_mass in enumerate(new_mass_values)]

# # Print updated mass values
# for i, body in enumerate(body_array):
#     print(f"Body {i + 1} - Mass: {body.mass}")



# -------------Better approach---------------
import numpy as np

class Body:
    def __init__(self, position, mass, radius):
        self.position = position
        self.mass = mass
        self.radius = radius

# Create instances of the Body class
b1 = Body(np.array([0, 0]), 10, 1)
b2 = Body(np.array([1, 1]), 15, 1)
b3 = Body(np.array([2, 2]), 20, 1)
b4 = Body(np.array([3, 3]), 25, 1)

# Create an array of instances
body_array = np.array([b1, b2, b3, b4])

# New mass values
new_mass_values = np.array([30, 35, 40, 45])

# Define a function to update the mass attribute
def update_mass(body, new_mass):
    body.mass = new_mass
    return body

# Vectorize the update_mass function
vectorized_update_mass = np.vectorize(update_mass, excluded=['new_mass'])

# Update mass values using vectorized operation
body_array = vectorized_update_mass(body_array, new_mass=new_mass_values)

# Print updated mass values
for i, body in enumerate(body_array):
    print(f"Body {i + 1} - Mass: {body.mass}")

