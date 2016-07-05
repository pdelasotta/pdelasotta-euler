# time         1.96 real         1.45 user         0.06 sys
import sys
import math

"""A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from
the product of two 3-digit numbers."""



def main():
    getBiggestPalindrome(999, 100)


def getBiggestPalindrome(maxN, minN):
    factors = (0,0,0)
    for i in range(maxN, minN, -1):
        for j in range(maxN, minN, -1):
            if checkFactors(i, j) and i * j > factors[2]:
                factors = (i, j, (i * j))
    print "Biggest palindrome is {0} = {1} * {2}".format(factors[2], factors[0], factors[1])


def checkFactors(x, y):
    return isNumPalindrome(x * y)


def isNumPalindrome(x):
    strx = str(x)
    if len(strx) % 2 != 0:
        return
    primeraMitad = strx[:len(strx) / 2]
    segundaMitad = (strx[len(strx) / 2:])[::-1]
    return primeraMitad == segundaMitad


if __name__ == '__main__':
    main()
