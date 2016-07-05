'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from __future__ import division
import sys


def main():
    suma = 2
    primos = [2]
    index = 0
    maximo = 2000000
    for i in range(3, maximo, 2):
        if not arrayContainsFactor(primos, i):
            primos.append(i)
            suma += i
            # print i
            # sys.stdout.write('.')
            # sys.stdout.flush()
    print suma
    return

def arrayContainsFactor(array, num):
    for elem in array:
        if(factors(num, elem)):
            return True
    return False

def isPrime(x):
    for i in range(x - 1, 2, -1):
        if factors(x,i):
            return False
    return True

def factors(x,y):
    return x%y==0


if __name__ == '__main__':
    main()
