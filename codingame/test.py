import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    num = int(input("Enter a number: "))

    ulonachi_numbers = []
    for i in range(2, num + 1):
        ulonachi_numbers.append(fibonacci(i))

    print("Ulonachi numbers up to and including", num, ":")
    for ulonachi_number in ulonachi_numbers:
        print(ulonachi_number)

if __name__ == "__main__":
    main()