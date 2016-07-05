import sys
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def isprime(x):
    for i in range(x - 1, 2, -1):
        if x % i == 0:
            return False
    return True


def isfactor(num, factor):
    return num % factor == 0

def main():
    x = 600851475143L
    print 'Buscando factor primo: ' + str(x)
    i = int(x/2)
    while i > 2:
        if isprime(i) and isfactor():
            print str(i)
            sys.exit(0)
        i -= 1


if __name__ == '__main__':
    main()
