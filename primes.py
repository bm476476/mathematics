def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def get_prime_numbers(n):
  primes = []
  for i in range(2, n + 1):
    if is_prime(i):
      primes.append(i)
  return primes

# Example usage
n = int(input("How many prime numbers do you want: "))

prime_numbers = get_prime_numbers(n)
print(f"The first {n} prime numbers are: {prime_numbers}")
