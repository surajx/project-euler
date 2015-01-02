#Programming not needed, Prime factorize and get the LCM

div_list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
num = 40
while True:
  gotReminder = False
  for div in div_list:
    if num%div!=0:
      gotReminder = True
      num+=20
      break
  if not gotReminder:
    print num
    break
