import matplotlib.pyplot as plt

mass = [65, 60, 55, 50, 45, 40, 35, 30, 25]
T1 = [0.898, 0.863, 0.826, 0.788, 0.747, 0.705, 0.659, 0.610, 0.557]
T2 = [0.887, 0.848, 0.823, 0.7825, 0.7765, 0.7005, 0.6705, 0.5995, 0.5625]

plt.figure(figsize=(10, 6))

# Plot T1
plt.plot(mass, T1, marker='o', linestyle='-', color='g', label='T1: Calculated points')

# Plot T2
plt.plot(mass, T2, marker='x', linestyle='--', color='b', label='T2: Experiment results')

# Adding titles and labels
plt.title('Period (T1 and T2) as Functions of Mass (Kg)')
plt.xlabel('(X 10^-3) Mass (Kg)')
plt.ylabel('Period (s)')
plt.grid(True)

# Adding the legend and moving it down slightly
plt.legend(loc='upper right', bbox_to_anchor=(1, 0.65))

# Show the plot
plt.show()