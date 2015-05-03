__author__ = 'Martin'


"""

Have the program find prime numbers
until the user chooses to stop
asking for the next one.

"""


pointer = 1


def get_primes():

    global pointer
    check = True

    while check:
        key = input("Press Enter to continue or X to exit")
        if key == 'X':
            check = False
        else:
            next_prime()
            pointer += 1


def next_prime():
    global pointer
    if all(pointer % i != 0 for i in range(2, pointer)):
        print(pointer)
    else:
        pointer += 1
        next_prime()


if __name__ == "__main__":
    get_primes()