import urllib.request  # Importing the urllib.request module to handle URL operations
import pandas as pd  # Importing pandas for data manipulation and analysis

# Downloading the COVID-19 dataset from a specified URL and saving it as 'italy-covid-daywise.csv'
urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv", "italy-covid-daywise.csv")

# Reading the downloaded CSV file into a pandas DataFrame
covid_df = pd.read_csv('italy-covid-daywise.csv')

# Converting the 'date' column to datetime format for easier manipulation
covid_df['date'] = pd.to_datetime(covid_df.date)

# Displaying information about the 'date' column
print(covid_df.date.info())

# Extracting the month from the 'date' column and creating a new column 'month'
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month

# Extracting the year from the 'date' column and creating a new column 'year'
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year

# Extracting the weekday from the 'date' column and creating a new column 'weekday'
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

# Printing the entire DataFrame to the console
print(covid_df)

# Saving the modified DataFrame back to the CSV file
covid_df.to_csv('italy-covid-daywise.csv',index=0)

# Filtering the DataFrame to include only the records from May (month == 5)
covid_df_may = covid_df[covid_df.month == 5]

# Creating a new DataFrame with selected columns: 'new_cases', 'new_deaths', 'new_tests'
covid_df_matrices = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Calculating and printing the mean of the selected columns
print(covid_df_matrices.mean())


