import pandas as pd

# Load the dataset
data = pd.read_csv('cancer_reg.csv')

# Inspect the data
print(data.info())
print(data.isnull().sum())

# Handle missing values
# Fill numeric columns with mean
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Fill categorical columns with mode
categorical_cols = data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Remove duplicates
data = data.drop_duplicates()

# Standardize column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# Save the cleaned dataset
data.to_csv('cancer_reg_cleaned.csv', index=False)