# Write A Program To Accept A String And Print It In The Reverse Order


# Method 1
x = str(input("Enter A String : "))
start = -1
print("The Reverse Order of ",x," is - ", end = "")
while start >= -(len(x)):
    letter = x[start]
    start = start - 1
    print(letter, end = "")


# Method 2
x = str(input("Enter A String : "))
print("The Reverse Order of ",x," is -",x[::-1], end = "")


# Method 3
x = str(input("Enter A String : "))
y = ""
for i in x:
    y = i + y
print(y)
