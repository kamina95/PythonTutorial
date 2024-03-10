import pandas as pd

# Simulated Customers Dataset
customers_data = {
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 34, 45, 23, 56],
    'location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
customers_df = pd.DataFrame(customers_data)

# Simulated Transactions Dataset
transactions_data = {
    'transaction_id': [10, 11, 12, 13, 14],
    'customer_id': [1, 2, 3, 4, 5],
    'date': ['2024-01-01', '2024-01-03', '2024-02-01', '2024-02-05', '2024-03-01'],
    'amount': [100, 150, 200, 250, 300]
}
transactions_df = pd.DataFrame(transactions_data)

# Merge the datasets on customer_id
merged_df = pd.merge(customers_df, transactions_df, on='customer_id')

print(merged_df)

# Group the data by location and sum the amounts
total_amount_by_location = merged_df.groupby('location')['amount'].sum()
print(total_amount_by_location)

# Group the data by location and sum the amounts
total_amount_by_location = merged_df.groupby('location')['amount'].sum()
print(total_amount_by_location)

# Categorize transactions
merged_df['transaction_size'] = pd.cut(merged_df['amount'], bins=[0, 100, 200, float('inf')],
                                       labels=['small', 'medium', 'large'])

# Calculate average age by transaction size
average_age_by_transaction_size = merged_df.groupby('transaction_size')['age'].mean()
print(average_age_by_transaction_size)

import matplotlib.pyplot as plt

# Plot Total Transactions Amount by Location
total_amount_by_location.plot(kind='bar')
plt.xlabel('Location')
plt.ylabel('Total Transaction Amount')
plt.title('Total Transactions Amount by Location')
plt.show()

# Plot Average Age of Customers by Transaction Size
average_age_by_transaction_size.plot(kind='bar', color='skyblue')
plt.xlabel('Transaction Size')
plt.ylabel('Average Age of Customers')
plt.title('Average Age of Customers by Transaction Size')
plt.show()


## EX1: Handling Missing Values
# Assume the merged dataset merged_df from the previous project might have missing
# values in the location and amount columns. The exercise involves identifying and
# handling these missing values.

# Simulate missing values
merged_df.loc[2, 'location'] = None  # Set one location to None
merged_df.loc[4, 'amount'] = None  # Set one amount to None

# Identify missing values
print("Missing Values:\n", merged_df.isnull().sum())

# Handling missing values
# Option A: Fill missing location with 'Unknown'
merged_df['location'].fillna('Unknown', inplace=True)

# Option B: Fill missing amount with the average amount
merged_df['amount'].fillna(merged_df['amount'].mean(), inplace=True)

# Verify the handling of missing values
print("\nAfter Handling Missing Values:\n", merged_df)

## EX2: Encoding Categorical Variables
# Categorical variables need to be encoded before they can be used in
# many types of analysis. Convert the location column into a numerical
# format using one-hot encoding.
# One-hot encode the 'location' column
location_encoded = pd.get_dummies(merged_df['location'], prefix='location')

# Join the encoded DataFrame back with the original DataFrame
merged_df_encoded = pd.concat([merged_df, location_encoded], axis=1)

# Display the encoded DataFrame
print(merged_df_encoded)

## EX3: Creating Pivot Tables
# Pivot tables are useful for summarizing data. Create a pivot table to
# analyze the average transaction amount by location and transaction size.

# Create a pivot table
pivot_table = merged_df.pivot_table(values='amount', index='location', columns='transaction_size', aggfunc='mean')

# Display the pivot table
print(pivot_table)


## EX4: Advanced Visualization Techniques
# Explore advanced visualization techniques by creating a heatmap of the pivot
# table created in Exercise 3, using seaborn.

import seaborn as sns
import matplotlib.pyplot as plt

# Ensure seaborn is installed: pip install seaborn

# Create a heatmap from the pivot table
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Average Transaction Amount by Location and Transaction Size')
plt.show()
