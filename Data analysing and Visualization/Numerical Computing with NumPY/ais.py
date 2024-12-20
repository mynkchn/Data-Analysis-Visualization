# Importing NumPy library
import numpy as np

# Creating a 3D NumPy array
arr = np.array([ 
    [[11, 12, 13, 14], 
     [13, 14, 15, 19]], 
    
    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 
    
    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])

# Array slicing in Numpy
print(arr[1:,1,:3])
print(arr.shape)

# Array accessing using index
print(arr[0,1,3])

# Reshaping an Array
print(arr.reshape(3,4,2))