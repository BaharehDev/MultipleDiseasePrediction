import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

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

# Split data into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the model
model = LogisticRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the results
print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{classification_report(y_test, y_pred, zero_division=0)}')
print(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')