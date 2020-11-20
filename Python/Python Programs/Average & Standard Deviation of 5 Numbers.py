# Write A Program To Obtain The Average and Standard Deviation of 5 Numbers

# Import Numpy for Numerical Calculations
import numpy as np

# Initiating an empty list
nums = []

# Creating a loop to ask 5 user inputs
for i in range(5):
    # Appending the empty list with the user inputs.
    nums.append(float(input(str(i+1) + ". Enter the numner: ")))


# Printing the average of the numbers input by the user.
print("The average of the 5 numbers is:", np.mean(nums))

# Printing the standard deviation of the numbers input by the user.
print("The standard deviation of the 5 numbers is:", np.std(nums))
