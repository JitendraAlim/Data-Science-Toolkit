# Write A Program To Obtain Reverse Of The Given Number

x = int(input("Enter A Number : "))
print("The Reverse Of The Number Is : ", end = "")

while x != 0:
    rem = x % 10
    x = x // 10
    print(rem, end = "")
