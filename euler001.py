
import sys


def euler001(max):
    sum = 0
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def main():
    print euler001(1000)


if __name__ == '__main__':
    main()
