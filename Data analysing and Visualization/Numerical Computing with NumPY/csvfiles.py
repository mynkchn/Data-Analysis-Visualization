import urllib.request  # Importing the urllib.request module to handle URL operations

# Retrieve climate data from a specified URL and save it to a local file 'climate.txt'
urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt'
)

import numpy as np  # Importing NumPy for numerical operations

# Load climate data from the text file, skipping the header and using comma as a delimiter
climate_data = np.genfromtxt("climate.txt", skip_header=1, delimiter=',')

# Define weights for the linear combination of climate factors
weights = np.array([0.3, 0.2, 0.5])

# Calculate yields by performing matrix multiplication between climate data and weights
yields = climate_data @ weights

# Concatenate the original climate data with the calculated yields
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)

# Save the concatenated results to a new text file 'climate_results.txt'
np.savetxt('climate_results.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yield_apples', 
           comments='')

# Print the results to the console
print(climate_results)
