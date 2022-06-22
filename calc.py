def num_sum(num1, num2):
    return num1 + num2


def num_subtraction(num1, num2):
    return num1 - num2


def num_multiplication(num1, num2):
    return num1 * num2


def num_division(num1, num2):
    return num1 / num2


def calculator(sign, input_list):
    if sign not in input_list:
        return "TypeError! Type math expression in right format (e.g.: 2 + 2)"
    index = input_list.index(sign)
    number1 = ''.join(input_list[:index])
    number2 = ''.join(input_list[(index+1):])
    if number1.isdigit() and number2.isdigit() is True:
        num1 = float(number1)
        num2 = float(number2)
        if sign == '+':
            return num_sum(num1, num2)
        elif sign == '-':
            return num_subtraction(num1, num2)
        elif sign == '*':
            return num_multiplication(num1, num2)
        elif sign == '/':
            return num_division(num1, num2)


def num_input():
    math_operation = input("Type in the math expression you'd like to complete:").replace(' ', '')
    if math_operation == 'e':
        return False
    li = list(math_operation)
    if '+' in li:
        return calculator('+', li)
    elif '-' in li:
        return calculator('-', li)
    elif '*' in li:
        return calculator('*', li)
    elif '/' in li:
        return calculator('/', li)
    elif '+' or '-' or '*' or '/' not in li:
        return "TypeError! Type math expression in right format (e.g.: 2 + 2)"
    else:
        return "TypeError! Type math expression in right format (e.g.: 2 + 2)"


def main():
    while True:
        n = num_input()
        print(n)
        if n is False:
            break


main()

# cd /Users/dmytrocash/Desktop/code/playground