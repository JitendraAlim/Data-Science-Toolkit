# Write a Python program to ask a user to input a number, and print whether it is prime.

# Taking input from the user.
n = int(input("Enter a number : "))

# Checking if the number is greater than 1. If not then else part will be executed.
if n > 1:

   # Checking if the input number is divisible by any number from 2 to the same number.
   for i in range(2,n):
       if (n % i) == 0:

           # If the number is divisible by any number, the user input is not a prime number.
           print(n, "is not a prime number.")
           break
   else:
       # If the number is not divisible by any number, the user input is a prime number.
       print(n, "is a prime number.")
       
else:
   print(n, "is not a prime number.")
