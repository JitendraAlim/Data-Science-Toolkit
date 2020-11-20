# Write A Program To Obtain The Smallest Number Among 5 Numbers

# Initiating an empty list
nums = []

# Creating a loop to ask 5 user inputs
for i in range(5):
    # Appending the empty list with the user inputs.
    nums.append(float(input(str(i+1) + ". Enter the numner: ")))


# Printing the smallest of the numbers input by the user.
print("The smallest of the 5 numbers is:", min(nums))
