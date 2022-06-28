class CustomError(Exception):
    def __init__(self, math_expression):
        self.math_expression = math_expression


class ZeroDivError(CustomError):
    def __str__(self):
        return '{} is invalid input. Dividing by zero is a silly ' \
               'thing to do!'.format(self.math_expression)


class WrongInputError(CustomError):
    def __str__(self):
        return '{} is invalid input. Type math expression in ' \
               'right format. E.g. 1 + 99'.format(self.math_expression)