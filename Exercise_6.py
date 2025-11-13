# Exercise 6: Pandas Series Creation and Indexing

import pandas as pd

celcius = [1, 12, 17, 20, 30, 37]

cel_series = pd.Series(celcius, name="Celcius")

fahrenheit_series = cel_series * 9/5 + 32
fahrenheit_series.name = "Fahrenheit"

# Display both Series
print(cel_series)
print(fahrenheit_series)
