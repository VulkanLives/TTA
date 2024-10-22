import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Define the desired number of sides (try changing this value!)
n_sides = 6

# Represent a die by using a numpy array
die = np.array([i for i in range(1, n_sides + 1)])

# Roll the die 20 times
n_rolls = 20

# Save the result of each roll
# First roll (same as before)
first_rolls = np.array([np.random.choice(die) for _ in range(n_rolls)])

# Second roll (code is the same but saved in a new numpy array)
second_rolls = np.array([np.random.choice(die) for _ in range(n_rolls)])

# Sum both rolls (this is easy since numpy allows vectorization)
sum_of_rolls = first_rolls + second_rolls

# Print mean, variance and covariance
print(f"mean of first_rolls: {np.mean(first_rolls):.2f}\nvariance of first_rolls: {np.var(first_rolls):.2f}\n")
print(f"mean of second_rolls: {np.mean(second_rolls):.2f}\nvariance of second_rolls: {np.var(second_rolls):.2f}\n")
print(f"mean of sum_of_rolls: {np.mean(sum_of_rolls):.2f}\nvariance of sum_of_rolls: {np.var(sum_of_rolls):.2f}\n")
print(f"covariance between first and second roll:\n{np.cov(first_rolls, second_rolls)}")

# Plot histogram
sns.histplot(sum_of_rolls, stat = "probability")
plt.show()


