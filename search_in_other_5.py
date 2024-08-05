import pandas as pd

# Load the datasets
df1 = pd.read_csv('dataset1.csv')  # Replace with your dataset1 file path
df2 = pd.read_csv('dataset2.csv')  # Replace with your dataset2 file path

# Specify the variables (columns) to search for in df1
variables = ['variable1', 'variable2', 'variable3']

# Create an empty dictionary to store the results
results = {var: [] for var in variables}

# Iterate through each variable
for var in variables:
    # Iterate through each value in the specified variable column in df1
    for value in df1[var]:
        # Check if the value exists in any cell of df2
        if df2.isin([value]).any().any():
            results[var].append(value)

# Print the results
for var, values in results.items():
    print(f"Values of {var} found in dataset2: {values}")
