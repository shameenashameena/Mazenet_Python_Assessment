# Exercise 8: DataFrame Plotting

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["A", "B", "A", "C", "B", "C", "A"],
    "Category": ["Electronics", "Clothing", "Electronics", "Furniture", 
                 "Clothing", "Furniture", "Electronics"],
    
    "Sales": [200, 150, 300, 400, 250, 350, 100]
}
df = pd.DataFrame(data)

cat_sal = df.groupby("Category")["Sales"].sum()

print(cat_sal)

cat_sal.plot(kind="bar", color="skyblue", title="Total sales per category")
plt.ylabel("Total Sales")
plt.show()
