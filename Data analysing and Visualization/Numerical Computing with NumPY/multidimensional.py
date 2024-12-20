
# Importing NumPy library
import numpy as np

# Creating a 2D NumPy array to hold climate data
climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
                         
# Printing the shape of the climate data array
print(climate_data.shape)

# Printing the data type of the climate data array
print(climate_data.dtype)

# Printing the item size of the climate data array
print(climate_data.itemsize)

# Defining weights for the linear combination of climate factors
weights = np.array([0.3, 0.2, 0.5])
print(weights.shape)

# Inbuilt function to perform matrix multiplication
yields = np.matmul(climate_data, weights)
print(yields)

# Another way to perform matrix multiplication
yields = climate_data @ weights
