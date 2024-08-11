import pandas as pd

# Sample DataFrame
data = {'Column1': [10, 20, 30, 40],
        'Column2': ['A', 'B', 'A', 'C']}
df = pd.DataFrame(data)

# Create a new variable (column) 'Column3' and assign values based on conditions in 'Column2'
df['Column3'] = 0  # Initialize the new column with default values

# Assign value to 'Column3' where 'Column2' has a certain value
df.loc[df['Column2'] == 'A', 'Column3'] = 100

print(df)

   Column1 Column2  Column3
0       10       A      100
1       20       B        0
2       30       A      100
3       40       C        0

