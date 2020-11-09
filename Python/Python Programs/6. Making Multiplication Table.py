# Write A Program To Obtain Multiplication Table Of A Number


x = int(input("Enter A Number : "))
y = 1

while y <= 10:
    z = x * y
    print(x,"*",y," = ",z)
    y = y + 1
print("End")
