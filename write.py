import pandas as pd

# Read the Excel file, ignoring the first row
df = pd.read_excel('LeetCode.xlsx', header=None, skiprows=[0])

# Get the values from the first column, removing characters until the dot
column_values = df.iloc[:, 0].apply(lambda x: x.split('.', 1)[-1])

# Write the values to a text file
with open('input.txt', 'w') as file:
    for value in column_values:
        file.write(str(value) + '\n')