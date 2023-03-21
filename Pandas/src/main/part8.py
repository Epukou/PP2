import pandas as pd

data = {
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'type': ['grass', 'fire', 'water', 'bug'],
    'hp': [45, 39, 44, 45],
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
    'pokedex': ['yes', 'no', 'yes', 'no']
}

pokemon = pd.DataFrame(data)

# reorder the columns
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]

# add a new column
pokemon['place'] = ['forest', 'mountain', 'ocean', 'meadow']

# display the data types of each column
print(pokemon.dtypes)
