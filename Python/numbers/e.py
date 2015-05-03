__author__ = 'Martin'

"""

Enter a number and have the program
generate e up to that many decimal places.
Keep a limit to how far the program will go.

"""


# Math.pi is a constant in math.py:14 - no args
import math
print("Constant from python module math.py: %f" % math.e)


# Source: http://stackoverflow.com/a/3559567

from decimal import *


def get_e(precision):
    getcontext().prec = precision
    return Decimal(1).exp()


if __name__ == '__main__':
    print(get_e(20))