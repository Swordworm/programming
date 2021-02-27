import numpy as np
import pylab


def function(x):
    return 2 * pow(x, 2) / 3


def calculate(xfrom, xto):
    xlist = np.arange(xfrom, xto, 0.01)
    ylist = [function(x) for x in xlist]
    pylab.plot(xlist, ylist)
    pylab.show()


def ask():
    numbers = input('Enter the range: ')
    list = numbers.split()
    length = len(list)
    if length == 1:
        print('You should enter two numbers.')
        ask()
    elif length > 2:
        print('To many numbers, you should enter only two of them.')
        ask()
    else:
        return numbers


fromAndTo = ask()
xFrom, xTo = fromAndTo.split()
xFrom = float(xFrom)
xTo = float(xTo)
calculate(xFrom, xTo)
