def is_pal(num):
  str_num = str(num)
  return str_num==str_num[::-1]

#Brute Forcing: Fails for 6 digit, better solution?
def get_largest_palindrome():
  lower1 = 99
  lower2 = 99
  large_num = 0
  for first_num in range(999,lower1,-1):
    for second_num in range(999,lower2,-1):
      num = first_num*second_num
      if is_pal(num):
        if large_num==0:
          large_num = num
          lower2 = second_num
          lower1 = second_num
          break
        else:
          if num>large_num:
            large_num=num
  return large_num

import time
start = time.time()
print get_largest_palindrome()
print time.time() - start
