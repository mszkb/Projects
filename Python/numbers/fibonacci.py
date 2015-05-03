__author__ = 'Martin'


"""

Enter a number and have the program
generate the Fibonacci sequence to
that number or to the Nth number.

"""

# Source http://en.literateprograms.org/Fibonacci_numbers_%28Python%29

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(7))