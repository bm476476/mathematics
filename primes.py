amountorLimit = str(input("Type in if you want to have the amount of primes or a start to limit of primes: "))
numberPrint = []

def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  numberPrint.append(n)
  return True

def startLimit():
  for i in range(start, limit):
    is_prime(i)


def amountOFPrimes():
  for i in range (0, 10000000):
    is_prime(i)
    if len(numberPrint) == amountOfPrimes:
      break

if amountorLimit == "Amount":
  amountOfPrimes = int(input("How many prime numbers do you want: "))
  amountOFPrimes()
elif amountorLimit == "Start to limit":
  start = int(input("What number do you want to start with: "))
  limit = int(input("What number do you want to end on: "))
  startLimit()



print(numberPrint)

  
