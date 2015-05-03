__author__ = 'Martin'


"""

Have the user enter a number and
find all Prime Factors (if there
are any) and display them.

"""


# Source: http://stackoverflow.com/a/16996439

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


if __name__ == '__main__':
    print(primes(80))