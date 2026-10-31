import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, np.nan, 30, 28, np.nan],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan, 'Phoenix']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# --------------------------------------------
# 1. Fill missing numeric values with mean
# --------------------------------------------
df_mean_filled = df.copy()
df_mean_filled['Age'] = df_mean_filled['Age'].fillna(df_mean_filled['Age'].mean())
print("\nAfter Filling Age with Mean:\n", df_mean_filled)

# --------------------------------------------
# 2. Fill missing numeric values with median
# --------------------------------------------
df_median_filled = df.copy()
df_median_filled['Age'] = df_median_filled['Age'].fillna(df_median_filled['Age'].median())
print("\nAfter Filling Age with Median:\n", df_median_filled)

# --------------------------------------------
# 3. Fill missing categorical values with mode
# --------------------------------------------
df_mode_filled = df.copy()
df_mode_filled['City'] = df_mode_filled['City'].fillna(df_mode_filled['City'].mode()[0])
print("\nAfter Filling City with Mode:\n", df_mode_filled)

# --------------------------------------------
# 4. Fill using forward fill (previous value)
# --------------------------------------------
df_ffill = df.copy()
df_ffill = df_ffill.fillna(method='ffill')
print("\nAfter Forward Fill:\n", df_ffill)

# --------------------------------------------
# 5. Fill using backward fill (next value)
# --------------------------------------------
df_bfill = df.copy()
df_bfill = df_bfill.fillna(method='bfill')
print("\nAfter Backward Fill:\n", df_bfill)

# --------------------------------------------
# 6. Replace all missing values with a constant
# --------------------------------------------
df_constant = df.copy()
df_constant = df_constant.fillna("Not Available")
print("\nAfter Constant Fill:\n", df_constant)

# --------------------------------------------
# 7. Drop rows with missing values
# --------------------------------------------
df_drop = df.dropna()
print("\nAfter Dropping Rows with Missing Values:\n", df_drop)
