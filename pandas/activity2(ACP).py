import pandas as pd
import numpy as np

data = {
    "Id": [1, 2, 3, 4],
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", np.nan, np.nan, np.nan],
    "Salary": [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
print("\n----------------------\n")

print("First 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))
print("\n----------------------\n")

print("Total null values:\n", df.isnull().sum())
print("\n----------------------\n")

print("DataFrame Info:")
print(df.info())
print("\n----------------------\n")

df_no_null_rows = df.dropna()
print("After dropping rows with null values:\n", df_no_null_rows)
print("\n----------------------\n")

df_no_null_cols = df.dropna(axis=1)
print("After dropping columns with null values:\n", df_no_null_cols)
print("\n----------------------\n")

df["Salary"].fillna(300, inplace=True)
print("After filling Salary nulls with 300:\n", df)
print("\n----------------------\n")

df["Role"].fillna("CEO", inplace=True)
print("After filling Role nulls with 'CEO':\n", df)