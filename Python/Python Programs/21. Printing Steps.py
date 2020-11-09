# Write A Python Program To Print The Following Pattern.
##                                        *
##                                        **
##                                        ***
##                                        ****

steps = int(input("Enter The Number Of Steps : "))
start = 1

while start <= steps:
     print( "*" * start )
     start = start + 1

print("Here Are Your",steps,"Steps")
