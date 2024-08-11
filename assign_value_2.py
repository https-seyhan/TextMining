import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['x', 'y', 'x', 'z']
})

# Use np.where to assign value to 'C' based on condition in column 'B'
df['C'] = np.where(df['B'] == 'x', df['A'] * 2, 0)
