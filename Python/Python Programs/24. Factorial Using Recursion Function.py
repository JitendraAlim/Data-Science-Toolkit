# Write A Python Program To Obtain Factorial Of A Number Using Recursion Function

def recfact(n):
     if n < 0 :
          return "Factorial Of Negative Number Doesn't Exist"
     elif n == 1 :
          return n
     elif n == 0 :
          return 1
     else :
          return n * recfact(n - 1)

n = int(input("Enter A Number : "))
print("Factorial Of", n ,"Is", recfact(n))

