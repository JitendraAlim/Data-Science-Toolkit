# Write A Python Program To Create A List With The First 100 Prime Numbers, And Print The Elements Of The List.

# Initiating an empty list
prime = []

n = 2

while len(prime) < 100:
  for i in range(2,n):
    if (n % i == 0):
      break
  else:
    prime.append(n)
  n = n + 1
  
print("First 100 prime numbers are: \n", prime, sep = "")
