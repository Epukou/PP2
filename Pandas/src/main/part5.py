import pandas as pd

raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
data1 = pd.DataFrame(raw_data_1)

raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
data2 = pd.DataFrame(raw_data_2)

raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
data3 = pd.DataFrame(raw_data_3)

# Join the two dataframes along rows
all_data = pd.concat([data1, data2])

# Join the two dataframes along columns
all_data_col = pd.concat([data1, data2], axis=1)

# Print data3
print(data3)

# Merge all_data and data3 along the subject_id value
merged_data = pd.merge(all_data, data3, on='subject_id')

# Merge only the data that has the same 'subject_id' on both data1 and data2
merged_data_same_id = pd.merge(data1, data2, on='subject_id')