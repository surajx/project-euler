def is_prime(n):
  if n <= 3:
    return n >= 2
  if n % 2 == 0 or n % 3 == 0:
    return False
  for i in range(5, int(n ** 0.5) + 1, 6):
    if n % i == 0 or n % (i + 2) == 0:
      return False
  return True

def get_nth_prime(n):
  prime_cnt = 1
  cur_num = 3
  while True:
    if is_prime(cur_num):
      prime_cnt+=1
      if prime_cnt==n:
        return cur_num
    cur_num+=2

print get_nth_prime(10001)
