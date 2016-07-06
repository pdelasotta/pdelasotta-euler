# -*- coding: utf-8 -*-
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
import sys
def main():
    answer = pow(2, 1000)
    stringAnswer = str(answer)
    listAnswer = list(stringAnswer)
    sumAnswer = 0
    for i in listAnswer:
        sumAnswer = sumAnswer + int(i)
    print sumAnswer

if __name__ == '__main__':
    main()
