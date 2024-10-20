# Given uncertainties
Delta_k = 0.09  # Uncertainty in k
Delta_D = 0.0003   # Uncertainty in D
Delta_d = 0.000027  # Uncertainty in d

# Known values for k, D, and d
k = 3.18       # Value of k
D = 0.0251    # Value of D
d = 0.000917   # Value of d

# Given value for N
N = 101  # Value of N

# Calculate G using the formula
G = (8 * N * k * D**3) / d**4

# Calculate Delta G using the error propagation formula
Delta_G = G * (abs(Delta_k / k) + abs(3 * Delta_D / D) + abs(4 * Delta_d / d))

# Print the results
print(f"G = {G:.4f}")
print(f"Delta G = {Delta_G:.4f}")