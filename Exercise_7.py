# Exercise 7: Pandas DataFrame Filtering

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 60000, 75000, 80000, 55000, 90000]
}

df = pd.DataFrame(data)

# 75th percentile of salary
salary_75 = df["Salary"].quantile(0.75)

# Filter employees with salary above 75th percentile
high_earners = df[df["Salary"] > salary_75]

print("75th Percentile Salary:", salary_75)
print(high_earners)
