import numpy as np

# Given values for mass (m) and period (T)
m_values = np.array([0.065, 0.060, 0.055, 0.050, 0.045, 0.040, 0.035, 0.030, 0.025])  # in kg
T_values = np.array([0.887, 0.848, 0.823, 0.7875, 0.7765, 0.7005, 0.6705, 0.5995, 0.5625])  # in seconds

# Calculate k1 for each mass using the formula k1 = (4 * pi^2 * m) / T^2
k_values = (4 * np.pi**2 * m_values) / (T_values**2)

# Calculate the average k
average_k = np.mean(k_values)

# Print the results
for i, k in enumerate(k_values):
    print(f"k1 for mass {m_values[i]} kg and period {T_values[i]} s is: {k:.4f} N/m")

# Print the average k value
print(f"\nAverage k = {average_k:.4f} N/m")