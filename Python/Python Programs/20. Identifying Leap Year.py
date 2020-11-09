# Write A Python Program To Check Whether The Entered Year Is A Leap Year.

# 2018 should not be Leap Year.
# 2020 should be a Leap Year.
# 2100 should not be a Leap Year.
# 2000 should be a Leap Year

# Method 1

year = int(input("Enter The Year You Wish To Check Is A Leap Year Or Not : "))

if year % 4 == 0:                                           # Divisible by 4
     if year % 100 == 0:                                   # Divisible by 4 & Not divisible by 100
          print(year,"Is A not Leap Year")
     elif year % 100 != 0:                                # Divisible by 4 & Divisible by 100
          if year % 400 == 0 :                             # Divisible by 4 & Divisible by 100 & Not divisible by 400
               print(year,"Is Not A Leap Year")
          else:                                                   # Divisible by 4 & Divisible by 100 & Divisible by 400
               print(year,"Is A Leap Year")
else:                                                             # Not divisible by 4
     print(year,"Is Not A Leap Year")

##
##if year % 4 == 0:
##     if (year % 100
##

# Method 2

x=int(input("Enter the year: "))
if (x%4==0 or (x%4==0 and x%100==0) ):
     print("Its a leap year",x)
else:
     print("its not a leap year")
     
