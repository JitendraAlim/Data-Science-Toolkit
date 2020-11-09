# Write A Program To Swap Two Numbers


# Method 1
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = a
a = b
b = c
print("New 1st Number Is :", a)
print("New 2nd Number Is :", b)


# Method 2
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
a,b = b,a
print("New 1st Number Is :", a)
print("New 2nd Number Is :", b)
