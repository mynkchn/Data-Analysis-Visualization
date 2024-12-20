# Importing the urllib.request module to handle URL operations
import urllib.request

# Downloading the COVID-19 data for Italy from a specified URL and saving it as a CSV file
urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv', 'italy-covid-daywise.csv')

# Importing the pandas library for data manipulation and analysis
import pandas as pd

# Reading the downloaded CSV file into a pandas DataFrame
covid_df = pd.read_csv('italy-covid-daywise.csv')

# Printing the 'new_cases' column from the DataFrame
print(covid_df.new_cases)

# Printing the 'date' and 'new_deaths' columns from the DataFrame
print(covid_df[["date","new_deaths"]])

# Printing the value of 'new_deaths' at index 247
print(covid_df.at[247,'new_deaths'])

# Creating a copy of the original DataFrame
covid_df_copy = covid_df.copy()

# Printing the row at index 243
print(covid_df.loc[243])

# Printing the first 5 rows of the DataFrame
print(covid_df.head(5))

# Printing the last 4 rows of the DataFrame
print(covid_df.tail(4))

# Printing the first valid index of the 'new_tests' column
print(covid_df.new_tests.first_valid_index())

# Printing a random sample of 10 rows from the DataFrame
print(covid_df.sample(10))

# Printing rows from index 108 to 113 (inclusive)
print(covid_df.loc[108:113])
