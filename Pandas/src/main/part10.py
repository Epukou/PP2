import pandas as pd
import numpy as np

wine = pd.read_csv('Pandas\src\main\wine.data', header=None)

# Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
wine = wine.drop(columns=[0, 3, 6, 8, 10, 12, 13])

# Assign the columns as below:
wine = wine.rename(columns={1: 'alcohol', 2: 'malic_acid', 3: 'alcalinity_of_ash', 5: 'flavanoids', 6: 'proanthocyanins', 8: 'hue'})

# Set the values of the first 3 rows from alcohol as NaN
wine.loc[:2, 'alcohol'] = np.nan

# Now set the value of the rows 3 and 4 of magnesium as NaN
wine.loc[2:3, 'magnesium'] = np.nan

# Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
wine['alcohol'] = wine['alcohol'].fillna(10)
wine['magnesium'] = wine['magnesium'].fillna(100)

# Count the number of missing values
print(wine.isna().sum())

# Create an array of 10 random numbers up until 10
# Use random numbers you generated as an index and assign NaN value to each of cell.
rand_index = np.random.choice(len(wine), 10)
wine.iloc[rand_index] = np.nan

# Delete the rows that contain missing values
wine = wine.dropna()

# Print only the non-null values in alcohol
print(wine.loc[wine['alcohol'].notna(), 'alcohol'])

# Reset the index, so it starts with 0 agai
wine = wine.reset_index(drop=True)