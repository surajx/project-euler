def is_prime(n):
  if n <= 3:
    return n >= 2
  if n % 2 == 0 or n % 3 == 0:
    return False
  for i in range(5, int(n ** 0.5) + 1, 6):
    if n % i == 0 or n % (i + 2) == 0:
      return False
  return True

def sum_primes_below_num(num):
  prime = 5
  prime_sum = 5
  while prime<num:
    if is_prime(prime):
      prime_sum+=prime
    prime+=2
  return prime_sum


import time
start = time.time()
print sum_primes_below_num(2000000)
print "Using is_prime check: ", time.time() - start

def sum_primes_sieve(limit):
  num_list = [num for num in range(2,limit,1)]
  list_idx=2
  while list_idx<len(num_list):
    num_list[list_idx] = 0
    list_idx+=2
  for num in num_list:
    if num>limit**(0.5):
      break
    if num==0:
      continue
    mul=3
    while True:
      multiple = num*mul
      if multiple>=limit:
        break
      else:
        num_list[multiple-2]=0
      mul+=2
  def uniqify(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]
  primes_list = uniqify(num_list)
  primes_list.remove(0)
  return sum(primes_list)

start = time.time()
print sum_primes_sieve(2000000)
print "Using Sieve of Eratosthenes check: ", time.time() - start




