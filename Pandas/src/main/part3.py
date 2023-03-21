import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv"

drinks = pd.read_csv(url, sep=",")

print("Which continent drinks more beer on average?\n ", drinks.groupby('continent')['beer_servings'].mean().idxmax())

print("Mean alcohol consumption per continent for every column\n ", drinks.groupby('continent').mean())

print("Median alcohol consumption per continent for every column\n ", drinks.groupby('continent').median())

print("Print the mean, min and max values for spirit consumption (This time output a DataFrame)\n", drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max']))

