#python --version 
#pip --version
#python -m pip install --upgrade pip
#pip install pandas
#pip install numpy

import pandas as pd
import numpy as np

# 1. Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles'],
    'Salary': [60000, 75000, 80000, 62000, 78000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# 2. Basic Data Exploration
print("DataFrame Info:")
df.info()
print("\n")

print("Descriptive Statistics:")
print(df.describe())
print("\n")

# 3. Data Manipulation and Analysis
# Calculate the average age
average_age = df['Age'].mean()
print(f"Average Age: {average_age:.2f}\n")

# Find the maximum salary
max_salary = df['Salary'].max()
print(f"Maximum Salary: {max_salary}\n")

# Filter data: people in New York
new_york_residents = df[df['City'] == 'New York']
print("New York Residents:")
print(new_york_residents)
print("\n")

# Group by City and calculate average salary for each city
average_salary_by_city = df.groupby('City')['Salary'].mean()
print("Average Salary by City:")
print(average_salary_by_city)