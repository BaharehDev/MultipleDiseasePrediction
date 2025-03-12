
blood_sample_dataset_balanced = pd.read_csv('/Users/bahar/Documents/IT-Högskolan/assignment3/dataset/Blood_samples_dataset_balanced_2(f).csv')
blood_samples_dataset_test = pd.read_csv('/Users/bahar/Documents/IT-Högskolan/assignment3/dataset/blood_samples_dataset_test.csv')

print('The balanced data is:')
print(blood_sample_dataset_balanced.head())
print(blood_sample_dataset_balanced.info())
print(blood_sample_dataset_balanced.isnull().sum())

print('\nThe test data is:')
print(blood_samples_dataset_test.head())
print(blood_samples_dataset_test.info())
print(blood_samples_dataset_test.isnull().sum())

print('\nblood_sample_dataset_balanced duplicated values:', blood_sample_dataset_balanced.duplicated().sum())
print('\nblood_sample_dataset_balanced duplicated values:', blood_samples_dataset_test.duplicated().sum())

clean_blood_sample_dataset_balanced = blood_sample_dataset_balanced.drop_duplicates()
print('\nDuplicates rows in blood_sample_dataset_balanced has removed. The result:', clean_blood_sample_dataset_balanced.duplicated().sum())

print('\nsummary statistics for numerical columns:', blood_sample_dataset_balanced.describe())

