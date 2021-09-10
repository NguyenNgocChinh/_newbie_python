from itertools import product
import string
import random

LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation


def password_generator(lenght=8):
    printable = f'{LETTER}{NUMBER}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=lenght)
    return ''.join(random_password)


def get_password_lenght():
    lenght = input('Press lenght password, must be digits: ')
    return int(lenght)


def main():
    lenght = get_password_lenght()
    password = password_generator(lenght)
    print(password)


if __name__ == '__main__':
    main()
