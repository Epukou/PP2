import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"

crime = pd.read_csv(url, sep=",")

# What is the type of the columns?
print(crime.dtypes)

# Convert the type of the column Year to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')

# Set the Year column as the index of the dataframe
crime.set_index('Year', inplace=True)

# Delete the Total column
crime.drop('Total', axis=1, inplace=True)

# Group the year by decades and sum the values
decade_crime = crime.resample('10AS').sum()

# What is the most dangerous decade to live in the US?
most_dangerous_decade = decade_crime['Violent'].idxmax().strftime('%Ys')
print("The most dangerous decade to live in the US was:", most_dangerous_decade)