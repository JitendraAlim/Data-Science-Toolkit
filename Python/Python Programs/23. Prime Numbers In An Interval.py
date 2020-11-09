# Write A Python Program To Print Prime Numbers In An Interval

lower = int(input("Enter The Lower Limit Of The Interval : "))
upper = int(input("Enter The Upper Limit Of The Interval : "))

print("The Prime Numbers From",lower,"To",upper,"Are :")

for number in range ( lower , upper + 1 ) :
     if number > 1:                                        # Prime Numbers are greater than 1
          for i in range ( 2 , number ) :           # To get all numbers till the selected number
               if ( number % i ) == 0 :                # If there is a divisor in preceeding numbers. Then remainder != 0 for some preceeding number
                    break
          else:                                                 # If there is no divisor in preceeding numbers. Then remainder = 0 for all preceeding numbers
                print(number)

     
