import pandas as pd
from sklearn.preprocessing import StandardScaler


# Load datasets
balanced_data = pd.read_csv('/Users/bahar/Documents/IT-Högskolan/assignment3/dataset/Blood_samples_dataset_balanced_2(f).csv')
test_data = pd.read_csv('/Users/bahar/Documents/IT-Högskolan/assignment3/dataset/blood_samples_dataset_test.csv')

# Check data information
print(balanced_data.info())
print(test_data.info())

# Check for missing values
print(balanced_data.isnull().sum())
print(test_data.isnull().sum())

# Remove duplicate rows
balanced_data = balanced_data.drop_duplicates()

# Convert numeric columns to float
balanced_data.iloc[:, :-1] = balanced_data.iloc[:, :-1].apply(pd.to_numeric, errors='coerce')

# Now calculate quantiles correctly
Q1 = balanced_data.select_dtypes(include=['number']).quantile(0.25)
Q3 = balanced_data.select_dtypes(include=['number']).quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Apply the filtering column by column
for col in balanced_data.select_dtypes(include=['number']).columns:
    balanced_data = balanced_data[(balanced_data[col] >= lower_bound[col]) & (balanced_data[col] <= upper_bound[col])]

# Standardize numerical data
scaler = StandardScaler()
# Separate numeric features and the target column
X = balanced_data.drop(columns=['Disease'])
y = balanced_data['Disease']  # Target column

# Standardize numerical data
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

