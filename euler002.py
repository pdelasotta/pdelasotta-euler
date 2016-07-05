import sys

def main():
    suma = 0
    prev = 0
    curr = 1
    fibs = 0
    while fibs < 4000000:
        fibs = prev + curr
        if fibs % 2 == 0:
            suma += fibs
        prev = curr
        curr = fibs
    print suma

if __name__ == '__main__':
    main()
