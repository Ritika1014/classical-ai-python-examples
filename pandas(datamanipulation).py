import pandas as pd
# 1. Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston'],
    'Salary': [50000, 60000, 45000, 52000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 2. View Data
print("\nHead:\n", df.head())
print("\nInfo:\n")
df.info()

# 3. Selecting Columns
print("\nSelect Column (Name):\n", df['Name'])
print("\nSelect Multiple Columns:\n", df[['Name', 'City']])

# 4. Row Filtering
print("\nRows where Age > 25:\n", df[df['Age'] > 25])

# 5. Add New Column
df['Bonus'] = df['Salary'] * 0.10
print("\nAfter Adding Bonus Column:\n", df)

# 6. Delete Column
df = df.drop(columns=['City'])
print("\nAfter Dropping City Column:\n", df)

# 7. Sorting
print("\nSorted by Salary:\n", df.sort_values('Salary'))

# 8. Handling Missing Values
df.loc[2, 'Age'] = None   # Add missing value
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nAfter Filling Missing Values:\n", df)

# 9. Grouping and Aggregation
grouped = df.groupby('Name')['Salary'].sum()
print("\nGroup by Name (Salary Sum):\n", grouped)

# 10. Merging Two DataFrames
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Department': ['HR', 'Finance']
})

merged = pd.merge(df, df2, on='Name', how='left')
print("\nMerged DataFrame:\n", merged)
