# Write A Program To Calculate The Area of Square, Rectangle, Circle And The Circumference Of The Circle


# Calculating Area Of Square
side = float(input("Enter The Side Of The Square : "))
area = side ** 2
print("Area Of The Square Is :",area, "sq. units")


# Calculating Area Of Rectangle
l = float(input("Enter The Length Of The Rectangle : "))
b = float(input("Enter The Breadth Of The Rectangle : "))
area = l * b
print("Area Of The Rectangle Is :",area, "sq. units")


# Calculating Area Of Circle
r = int(input("Enter The Radius Of The Circle : "))
area = (22/7) * r**2
print("Area Of The Circle Is :",area, "sq. units")


# Calculating Circumference Of Circle
r = int(input("Enter The Radius Of The Circle : "))
circumference = 2 * (22/7) * r
print("Circumference Of The Circle :",circumference, "units")
