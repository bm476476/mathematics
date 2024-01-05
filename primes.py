
limit = int(input("Type in the value you don't want to exceed: "))
start = int(input("Type in the value you want to start at (type in 0 if no value is wanted): "))
amountOfPrimes = int(input("Type in the amount of prime numbers you want to print: "))
numberPrint = []

def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  numberPrint.append(n)
  return True

for i in range(start, limit):
  if start == 0:
    break  
  is_prime(i)

for i in range (0, 10000000):
  is_prime(i)
  if len(numberPrint) == amountOfPrimes:
      break

print(numberPrint)

  
