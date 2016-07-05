import sys

"""2520 is the smallest number that can be
divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
 divisible by all of the numbers from 1 to 20?"""


def main():
    result = 0
    num = 0
    while not result:
        num += 20
        print num
        if(checkFactors(num)):
            result = num

    print result


def checkFactors(x):
    result = True
    for i in range(20, 1, -1):
        if x % i != 0:
            result = False
            break
    return result

if __name__ == '__main__':
    main()
