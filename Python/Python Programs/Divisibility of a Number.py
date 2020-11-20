# Write a Python program to aAsk a user to input a number, and print whether it is divisible by 5.

# Taking an input from the user.
num = int(input("Enter a number: "))

# Checking if the number is divisible by 5.
if num % 5 == 0:
    # Output if the number is divisible by 5.
    print(num, "is divisible by 5.")
else:
    # Output if the number is not divisible by 5.
    print(num, "is not divisible by 5.")
