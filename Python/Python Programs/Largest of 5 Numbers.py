# Write A Program To Obtain The Largest Number Among 5 Numbers

# Initiating an empty list
nums = []

# Creating a loop to ask 5 user inputs
for i in range(5):
    # Appending the empty list with the user inputs.
    nums.append(float(input(str(i+1) + ". Enter the numner: ")))


# Printing the largest of the numbers input by the user.
print("The largest of the 5 numbers is:", max(nums))
