from .exceptions import ZeroDivError, WrongInputError


def num_sum(num1, num2):
    return num1 + num2


def num_subtraction(num1, num2):
    return num1 - num2


def num_multiplication(num1, num2):
    return num1 * num2


def num_division(num1, num2):
    return num1 / num2


def calculator(char_input):
    operations = {
        "+": num_sum,
        "-": num_subtraction,
        "*": num_multiplication,
        "/": num_division
    }

    char_list = []
    num = ''
    operation_symbol = ''
    for char in char_input:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                char_list.append(num)
                num = ''
            if char in operations:
                operation_symbol = char
                char_list.append(operation_symbol)
            else:
                raise WrongInputError(char_input)
    if num != '':
        char_list.append(num)
    if len(char_list) != 3:
        raise WrongInputError(char_input)
    calculation_function = operations[operation_symbol]
    num1 = int(char_list[0])
    num2 = int(char_list[2])

    try:
        return calculation_function(num1, num2)
    except ZeroDivisionError:
        raise ZeroDivError(char_input)

