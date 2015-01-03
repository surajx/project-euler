#a+b+c=1000
#a**2 + b**2 = c**2
#c10**6 - 2000c**2 = 2abc

a=1
b=1
c=1000-(a+b)
is_not_triplet = a**2+b**2!=c**2
while is_not_triplet:
  a+=1
  b=1
  c=1000-(a+b)
  while c>a and c>b:
    b+=1
    c=1000-(a+b)
    is_not_triplet = a**2+b**2!=c**2
    if not is_not_triplet:
      break
print a*b*c
