
import pandas as pd
import matplotlib.pyplot as plt

# Creating the Users dataset
data_users = {
    'user_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [28, 34, 45, 23]
}
users = pd.DataFrame(data_users)

# Creating the Purchases dataset
data_purchases = {
    'purchase_id': ['A1', 'A2', 'B1', 'C1', 'C2', 'D1'],
    'user_id': [1, 1, 2, 3, 3, 4],
    'item': ['Book', 'Pen', 'Pencil', 'Notebook', 'Eraser', 'Stapler'],
    'amount_spent': [15, 3, 2, 20, 5, 10]
}
purchases = pd.DataFrame(data_purchases)

# Display the datasets
print("Users Dataset:")
print(users)
print("\nPurchases Dataset:")
print(purchases)


# Merge the datasets on 'user_id'
combined_data = pd.merge(users, purchases, on='user_id')

print("\nCombined Dataset:")
print(combined_data)


# Calculate the total amount spent by each user
total_spent = combined_data.groupby('name')['amount_spent'].sum().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(total_spent['name'], total_spent['amount_spent'], color='skyblue')
plt.xlabel('User')
plt.ylabel('Total Amount Spent ($)')
plt.title('Total Amount Spent by Each User')
plt.xticks(rotation=45)
plt.show()
