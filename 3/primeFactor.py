def is_prime(n):
  if n <= 3:
    return n >= 2
  if n % 2 == 0 or n % 3 == 0:
    return False
  for i in range(5, int(n ** 0.5) + 1, 6):
    if n % i == 0 or n % (i + 2) == 0:
      return False
  return True

def is_prime_aks(n):
  #AKS primality test is in P
  #http://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf
  pass

def rev_factoring(num):
  effective_boundary = int(num ** 0.5) + 1
  step = -1
  for val in range(effective_boundary, 5, step):
    if is_prime(val):
      step = -6
      if num%val==0:
        return val

print rev_factoring(600851475143)
