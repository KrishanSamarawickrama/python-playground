import sys

def collatz(number):
    if(number % 2 == 0):
        val = number // 2
    else:
        val = 3 * number + 1
    print(val)
    if val == 1:
        sys.exit()


while True:
    print('Enter number:')
    try:
        number = int(input())
    except ValueError:
        print('Input a valid number')
    collatz(number)
