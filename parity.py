"""
Parity
"""


def print_number_parity(number):
    parity = number % 2
    print(parity)


def get_number_parity(number):
    parity = number % 2
    return parity

def is_odd(number):
    if number%2 == 0:
        return False
    else:
        return True

    

def main():
    print(f"Parity of 4 should be 0:")
    print_number_parity(4)
    print(f"Parity of 41 should be 1:")
    print_number_parity(41)

    print(f"Parity of 4 should be 0:", get_number_parity(4))
    print(f"Parity of 41 should be 1:", get_number_parity(41))

    print(f"The number 3 is odd : True ",is_odd(3))
    print(f"The number 2 is odd : False ",is_odd(2))


main()
