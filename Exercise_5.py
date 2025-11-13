# Exercise 5: NumPy Array Manipulation

import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)

diag_matrix = np.diag(matrix)

diag_sum_matrix = np.sum(diag_matrix)

print("Matrix:\n", matrix)
print("Diagonal elements:", diag_matrix)
print("Sum of diagonal elements:", diag_sum_matrix)


