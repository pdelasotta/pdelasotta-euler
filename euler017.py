# -*- coding: utf-8 -*-
# time 0.06 real         0.04 user         0.01 sys
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# ugly code but it works and i'm lazy
import sys
def main():
    sumLength = 0
    for i in range(1, 1001):
        print worder(i), len(worder(i))
        sumLength = sumLength + len(worder(i))
    print sumLength

def worder(i):
    if(i < 10):
        return digitToWord(i)
    elif(i < 20):
        return overNine(i)
    elif(i < 100):
        return overNineTeen(i)
    elif(i < 1000):
        return over99(i)
    else:
        return "onethousand"

def digitToWord(digit):
    digitDictionary = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    return digitDictionary[digit]

def overNine(teen):
    teenDictionary = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    return teenDictionary[teen]

def overNineTeen(overNineteen):
    firstDigit = int(str(overNineteen)[0])
    secondDigit = int(str(overNineteen)[1])
    overNineteenDictionary = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    answer = overNineteenDictionary[firstDigit]
    if(secondDigit != 0):
        answer = answer +digitToWord(secondDigit)
    return answer

def over99(over99):
    firstDigit = int(str(over99)[0])
    secondDigit = int(str(over99)[1])
    thirdDigit = int(str(over99)[2])
    answer = digitToWord(firstDigit) + "hundred"
    if(secondDigit > 0 or thirdDigit > 0):
        answer = answer + "and"
    if(secondDigit > 0):
        if(secondDigit == 1):
            answer = answer + overNine(secondDigit*10+thirdDigit)
            return answer
        elif(secondDigit > 1):
            answer = answer + overNineTeen(secondDigit*10+thirdDigit)
            return answer
    elif(thirdDigit > 0):
        answer = answer + digitToWord(thirdDigit)
    return answer

if __name__ == '__main__':
    main()
