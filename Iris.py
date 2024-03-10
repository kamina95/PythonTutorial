import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, names=columns)

# View the first few rows of the dataset
print(iris.head())

# Describe the dataset to get summary statistics
print(iris.describe())

# Filter the data for setosa species
setosa = iris[iris['species'] == 'Iris-setosa']
print(setosa.head())


# Create a scatter plot for sepal length vs. sepal width, color-coded by species
species_colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
for species, color in species_colors.items():
    subset = iris[iris['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], label=species, color=color)

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width by Species')
plt.legend()
plt.show()


# Calculate the mean sepal length for each species
mean_sepal_length = iris.groupby('species')['sepal_length'].mean()
print(mean_sepal_length)

# Find the correlation between sepal length and sepal width
correlation = iris['sepal_length'].corr(iris['sepal_width'])
print(f"Correlation between sepal length and sepal width: {correlation}")
