import numpy as np
import matplotlib.pyplot as plt

# Data: years and revenue
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
revenues = np.array([253667, 288226, 185943, 313849, 347684, 374377, 308450, 331026, 433300, 490675])

# Shift years to start from 0 for simplicity (2014 -> 0, ..., 2023 -> 9)
years_shifted = years - 2014

# Fit a cubic polynomial (degree 3)
coeffs = np.polyfit(years_shifted, revenues, 3)
polynomial = np.poly1d(coeffs)

# Generate x values for plotting the polynomial
x_vals = np.linspace(0, 9, 100)
y_vals = polynomial(x_vals)

# Plot the data and the polynomial
plt.figure(figsize=(10, 6))
plt.scatter(years, revenues, color='red', label='Actual Data')
plt.plot(x_vals + 2014, y_vals, label=f'Fitted Polynomial: {polynomial}', color='blue')
plt.xlabel('Year')
plt.ylabel('Revenue (RM\'000)')
plt.title('Revenue vs. Year with Fitted Polynomial')
plt.legend()
plt.grid(True)
plt.show()

print(f"Fitted Polynomial Equation:\n{polynomial}")
