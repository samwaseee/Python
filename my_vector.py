import numpy as np

# Define vectors
v1 = np.array(list(map(int, input("Enter vector v1 :").split())))
v2 = np.array([4, 5, 6])

# Vector addition
v_sum = v1 + v2
print("Sum:", v_sum)

# Dot product
dot_product = np.dot(v1, v2)
print("Dot Product:", dot_product)

# Magnitude of a vector
magnitude = np.linalg.norm(v1)
print("Magnitude of v1:", magnitude)
