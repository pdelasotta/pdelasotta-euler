# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.
import sys
import math


def main():
    print squareOfSum(100) - sumOfSquares(100)


def sumOfSquares(maxN):
    suma = 0
    for n in range(1, maxN + 1):
        suma += n ** 2
    return suma


def squareOfSum(maxN):
    suma = 0
    for n in range(1, maxN + 1):
        suma += n
    return suma ** 2


if __name__ == '__main__':
    main()
