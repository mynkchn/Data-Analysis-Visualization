# Importing the urllib.request module to handle URL operations
import urllib.request

# Downloading the COVID-19 data for Italy from a specified URL and saving it as a CSV file
urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv', 'italy-covid-daywise.csvt')

# Importing the pandas library for data manipulation and analysis
import pandas as pd

# Reading the downloaded CSV file into a pandas DataFrame
covid_df = pd.read_csv('italy-covid-daywise.csv')

# Printing the type of the DataFrame to confirm it has been loaded correctly
print(type(covid_df))

# Displaying a summary of the DataFrame, including the index dtype and columns, non-null values, and memory usage
print(covid_df.info())

# Generating descriptive statistics for the DataFrame, including count, mean, std, min, and max values
print(covid_df.describe())

# Printing the shape of the DataFrame to show the number of rows and columns
print(covid_df.shape)
