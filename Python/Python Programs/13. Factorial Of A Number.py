# Write A Program To obtain The Factorial Of A Number

x = int(input("Enter a number : "))
fact = 1
while x > 0:
    fact = fact * x
    x = x - 1
print("Factorial of x = ", fact) 



