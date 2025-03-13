
# Problem Description
The problem I aim to solve is to interpret patient data in order to predict the risk of certain diseases. The dataset I am using contains information from blood samples, and the goal is to predict whether the patient has a particular disease based on the features of the sample.

In this project, I will:

- Investigate and preprocess the dataset.
- Train a machine learning model to predict disease risk using logistic regression.
- Evaluate the model's performance by calculating its accuracy and analyzing its classification report and confusion matrix.
## Dataset Description
The dataset consists of two CSV files:

1. Balanced Dataset - This dataset contains labeled blood sample data that has been preprocessed to address any imbalances in the data.
Test Dataset - This dataset is used for final testing of the model and will be evaluated after the model is trained.
Both datasets have several columns, including the target column, "Disease," which indicates whether the patient has the disease (1) or not (0). The features consist of numerical measurements from the blood samples.

2. Rows: The balanced dataset has several hundred rows, while the test dataset contains a smaller number of rows for evaluation.
Columns: The columns contain numerical features that describe various aspects of the blood samples, such as counts of different cells and chemicals, as well as the "Disease" column, which is the target variable.

## Data Exploration.
Before starting the model implementation, the following steps are performed to understand and preprocess the data:

1. Missing Values Check:
- I checked both datasets for any missing values.
- Any rows with missing values were handled accordingly.

2. Removing Duplicates:
- Duplicates were removed from the balanced dataset to ensure clean data.

3. Converting Data Types:
- The numeric columns were converted to float types to ensure they are processed correctly by the model.

4. Handling Outliers:
- I calculated the Interquartile Range (IQR) to detect and filter out any extreme values that could affect the model's performance.

5. Data Scaling:
- Standardization was applied to the numeric features to ensure the data has a mean of 0 and a standard deviation of 1. This is important for the model to perform efficiently.

## Problem Type
This problem is a classification problem because the goal is to predict whether a patient has a disease or not (binary classification). The dataset is labeled, meaning that it already contains the target variable, "Disease," which provides the answers to the model during training.

Since the dataset is well-suited for supervised learning, I will be using logistic regression as the model to solve this classification problem.

## Model Choice
- Model: I have chosen to use Logistic Regression, a commonly used algorithm for binary classification problems. It is simple to implement, interpretable, and works well with linearly separable data.

## Data Compatibility
The dataset contains numerical features, which are suitable for training machine learning models. All non-numeric columns have been handled (e.g., converting them to numeric where necessary). The data was also standardized to ensure that all features are on a comparable scale.

## Steps Performed in the Code
1. Loading the Data: The dataset is loaded into pandas DataFrames.

2. Data Preprocessing:
- Checked for missing values and removed duplicates.
- Converted columns to numeric format.
- Applied the IQR method to remove outliers.

3. Data Scaling: The features (X) are scaled using StandardScaler, which standardizes the data.

4. Train-Test Split: The data is split into training and test sets (80% for training, 20% for testing).

5. Model Training: I initialized a Logistic Regression model and trained it using the training data.

6. Model Evaluation:

- Accuracy is calculated using the accuracy_score function.
- A classification report is generated to evaluate the model’s performance in terms of precision, recall, and F1-score.
- A confusion matrix is printed to visualize the model's performance.

## Challenges and Considerations
- Data Quality: The dataset required several preprocessing steps, including handling missing values, duplicates, and outliers. These steps were necessary to ensure the data was clean and ready for modeling.
- Model Selection: While logistic regression works well for this type of problem, it is important to experiment with other models (e.g., Decision Trees, Random Forests) to see if they can improve the performance.

### dataset resource
https://www.kaggle.com/datasets/ehababoelnaga/multiple-disease-prediction