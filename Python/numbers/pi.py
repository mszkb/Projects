__author__ = 'Martin'

"""

Enter a number and have the program generate PI
up to that many decimal places.
Keep a limit to how far the program will go.

"""


# Math.pi is a constant in math.py:14 - no args
import math
print("Constant from python module math.py: %f" % math.pi)


import decimal


def arch_pi(precision=30):
    # x: circumference of the circumscribed (outside) regular polygon
    # y: circumference of the inscribed (inside) regular polygon

    if precision > 30:
        precision = 30
        print('Only 30 digits allowed')

    decimal.getcontext().prec = precision+1
    D = decimal.Decimal

    # max error allowed
    eps = D(1)/D(10**precision)

    # initialize w/ square
    x = D(4)
    y = D(2)*D(2).sqrt()

    ctr = D(0)
    while x-y > eps:
        xnew = 2*x*y/(x+y)
        y = D(xnew*y).sqrt()
        x = xnew
        ctr += 1

    return str((x+y)/D(2))


if __name__ == '__main__':
    print(arch_pi(20))