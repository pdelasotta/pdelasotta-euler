'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import sys
'''
import math
'''


def main():
  for i in range(1000):
      a = i
      for j in range(1000):
          b = j
          c = 1000 - (a + b)
          if(isGreaterThanBoth(a,b,c)):
              if isPithagorean(a,b,c):
                  result = [a,b,c]
                  print result
                  print a*b*c
                  return

  print result


def square(n):
  return n*n

def isPithagorean(a,b,c):
  return square(a)+square(b)==square(c)

def isGreaterThanBoth(a,b,c):
    return (c > a and c > b)

if __name__ == '__main__':
    main()
