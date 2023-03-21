import pandas as pd

url_1 = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
df = pd.read_csv(url_1, sep='|')
users = pd.read_csv(url_1, sep='|', index_col='user_id')

print("See the first 25 entries\n", users.head(25))

print("See the last 10 entries\n", users.tail(10))

print("Number of observations:-", len(users))

print("Number of columns:", len(users.columns))

print("Columns in the dataset:", list(users.columns))

print("Index of the dataset:", users.index.name)

print("Data types of each column:\n", users.dtypes)

print("Occupation column:\n", users['occupation'])

print("Number of different occupations:", users['occupation'].nunique())

print("Most frequent occupation:", users['occupation'].value_counts().idxmax())

print("Summary of the DataFrame:\n", users.describe())

print("Summary of all the columns:\n", users.describe(include='all'))

print("Summary of only the occupation column:\n", users['occupation'].describe())

print("Mean age of users:", users['age'].mean())

print("Age with least occurrence:", users['age'].value_counts().tail(1).index[0])

url_2 = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
df = pd.read_csv(url_2, sep='|')