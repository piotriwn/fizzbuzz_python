""" Fizz Buzz is a game where you count up from 1, substituting "fizz" for
multiples of 3, "buzz" for multiples of 5, and "fizzbuzz" for multiples
of 3 and 5.
"""

import sys

def calc(n):
    div5 = (n % 5 == 0)
    div3 = (n % 3 == 0)
    return (div5, div3)


if __name__ == '__main__':
    while True:
        print("Please input a natural number or press [0] to exit")
        inpt = input()
        print("---")
        if inpt == '0':
            sys.exit()
        elif inpt.isdecimal() == False:
            continue
        elif (int(inpt) < 0):
            continue
        else:
            intinpt = int(inpt)
            for i in range(1,intinpt+1):
                ituple = calc(i)
                if ituple ==  (1,1):
                    print("FizzBuzz")
                elif ituple == (1,0):
                    print("Buzz")
                elif ituple == (0,1):
                    print("Fizz")
                else:
                    print(str(i))
                


