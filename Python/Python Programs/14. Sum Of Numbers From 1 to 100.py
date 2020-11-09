# Write A Progam To Obtain The Sum Of Numbers From 1 To 100

# Method 1
x = 1
y = 0
while x<101:
    y = y + x
    x = x + 1

print("The Sum Of Numbers From 1 To 100 is ",y)

# Method 2
y = 0

for x in range(1,101):
    y = y + x
print("The Sum Of Numbers From 1 To 100 is ",y)
