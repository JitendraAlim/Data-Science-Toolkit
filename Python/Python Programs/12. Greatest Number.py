# Write A Program To Obtain The Greatest Number Among 3 Numbers


a = float(input("Enter 1st Number : "))
b = float(input("Enter 2nd Number : "))
c = float(input("Enter 3rd Number : "))
print(a,b,c)

if a >= b and a >= c:
    print(a,"Is The Greatest Number")
elif b >= a and b >= c:
    print(b,"Is The Greatest Number")
else:
    print(c,"Is The Greatest Number")
