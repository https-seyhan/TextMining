import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['x', 'y', 'x', 'z']
})

# Assign a value to a new column 'C' based on a condition on column 'B'
df = df.assign(C=lambda x: x['A'] * 2 if x['B'] == 'x' else 0)
