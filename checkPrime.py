#!/usr/bin/python3
import pdb
def check_prime(x):
  if x == 2:
    print("%s is a prime number" %(x))
  if x == 0 or x == 1:
    print("%s is a not prime number" %(x))
  else:
    fail = False
    for i in range(2, x):
      if x % i == 0:
        fail = True
        break
    if fail:
      print("%s is a not prime number" %(x))
    else:
      print("%s is a prime number" %(x))

check_prime(int(input("Enter a number: ")))
