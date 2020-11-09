# Write A Python Program To Calculate GCD Of Two Numbers.

num1 = int(input("Enter The 1st Number : "))
num2 = int(input("Enter The 2st Number : "))

# First We Remove (-ve) Sign. Cause (-ve) Sign Doesn't Make Difference While Calculating GCD.
mod1 = abs(num1)
mod2 = abs(num2)

# Now To Calculate GCD, We First Check Which Number Is Large And Which Is Small

if mod1 > mod2:
     large = mod1
     small = mod2
else:
     large = mod2
     small = mod1
if small!=0:
     for i in range ( 1 , small + 1 ) :
          if ( large % i == 0 ) and ( small % i == 0 ) :
               gcd = i
     print(gcd)
else:
     print("gcd=",large)
