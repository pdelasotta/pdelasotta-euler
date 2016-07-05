# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
#  can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
import sys


def main():
    primesFound = 2
    num = 3
    while primesFound < 10001:
        num += 2
        if(isprime(num)):
            primesFound += 1
            print primesFound
    print num

def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
