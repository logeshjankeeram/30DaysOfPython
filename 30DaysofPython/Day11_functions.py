import numpy as np

# Given values
p_mean = 3.982 * 10**-7
p_values = [
    3.949 * 10**-7,
    4.390 * 10**-7,
    4.147 * 10**-7,
    3.658 * 10**-7,
    3.766 * 10**-7
]

# Calculate squared deviations
squared_deviations = [(p_mean - p_i)**2 for p_i in p_values]

# Sum of squared deviations
total_squared_deviations = sum(squared_deviations)

# Number of observations
n = len(p_values)

# Calculate s using the provided formula
s = np.sqrt(total_squared_deviations / (n * (n - 1)))

# Print the result
print("Calculated value of s:", s)