from exceptions import ZeroDivError, WrongInputError
from calc import calculator


def main():
    print('Welcome to calculator. You can do operations with two integers and '
          'followed mathematical signs: +, -, *, /. For exit type "e".')
    while True:
        try:
            char_input = input("Type in the math expression you'd like to "
                               "complete:").replace(' ', '')
            if char_input == 'e':
                return False
            c = calculator(char_input)
            print(c)
            if c is False:
                break

        except (ZeroDivError, WrongInputError) as exc:
            print(exc)


if __name__ == '__main__':
    print(main())
