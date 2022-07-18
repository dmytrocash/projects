class CustomError(Exception):
    def __init__(self, math_expression):
        self.math_expression = math_expression


class ZeroDivError(CustomError):
    def __str__(self):
        return 'Dividing by zero is a silly thing to ' \
               'do!'


class WrongInputError(CustomError):
    def __str__(self):
        return 'Invalid input. Type math expression in ' \
               'right format. E.g. 1 + 99'
