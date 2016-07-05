# -*- coding: utf-8 -*-
# time        34.12 real        32.83 user         0.35 sys
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#

import sys

def main():
    collatzDictionary = {}
    for i in range(999999, 0, -1):
        collatzLength = getCollatzLength(i)
        collatzDictionary.update({collatzLength: i})
    maxKey = getMaxKey(collatzDictionary)
    print "Maximum length of chain " + str(maxKey)
    print "Starting number " + str(collatzDictionary[maxKey])

def getMaxKey(dictionary):
    return max(dictionary.keys(), key=int)

def getCollatzLength(number):
    current = number
    collatzLength = 0
    while current > 1:
        collatzLength = collatzLength + 1
        if(current % 2 == 0):
            current = collatzEven(current)
        else:
            current = collatzOdd(current)
    if (current == 1):
        collatzLength = collatzLength+1
    return collatzLength

def collatzEven(n):
    return n/2
def collatzOdd(n):
    return (3*n)+1

if __name__ == '__main__':
    main()
