# Importing the urllib.request module to handle URL operations
import urllib.request
import matplotlib.pyplot as plt

# Downloading the COVID-19 data for Italy from a specified URL and saving it as a CSV file
urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv", "italy-covid-daywise.csv")

# Downloading the locations data for Italy from a specified URL and saving it as a CSV file
urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')

# Importing the pandas library for data manipulation and analysis
import pandas as pd 

# Reading the downloaded COVID-19 data into a pandas DataFrame
covid_df = pd.read_csv('italy-covid-daywise.csv')

# Reading the locations data into a pandas DataFrame
location_df = pd.read_csv('locations.csv')

# Calculating the total number of new cases reported
total_cases = covid_df.new_cases.sum()

# Calculating the total number of new deaths reported
total_deaths = covid_df.new_deaths.sum()

# Printing the total number of reported cases and deaths
print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))

# Calculating the death rate as a proportion of new deaths to new cases
death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()

# Printing the death rate as a percentage
print('The death rate is {:.2f}% .'.format(death_rate))

# Initial number of tests conducted
initial_tests = 935310

# Calculating the total number of tests conducted
total_tests = initial_tests + covid_df.new_tests.sum()

# Calculating the positive rate as a proportion of total cases to total tests
positive_rate = total_cases / total_tests

# Printing the percentage of tests that resulted in a positive diagnosis
print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate * 100))

# Setting the date column as the index for the DataFrame
covid_df.set_index('date', inplace=True)

# Calculating cumulative sums for total cases, deaths, and tests
covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests

# Plotting the total cases, deaths, and tests over time
covid_df.total_cases.plot(label='Total Cases')
covid_df.total_deaths.plot(label='Total Deaths')
covid_df.total_tests.plot(label='Total Tests')
plt.title('COVID-19 Total Cases and Deaths in Italy')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()

# Adding a location column to the DataFrame
covid_df['location'] = 'Italy'

# Merging the COVID-19 data with location data
merged_df = covid_df.merge(location_df, on="location")

# Saving the merged DataFrame to a CSV file
merged_df.to_csv('merged.csv', index=0)

# Importing the sqlalchemy to perform sql operations
from sqlachemy import create_engine

# Create a database connection (using SQLite for this example)
engine = create_engine('sqlite://mydatabase')

# Saving the merged DataFrame to a SQL database
merged_df.to_sql('merged', con=engine, if_exists='replace', index=False)

