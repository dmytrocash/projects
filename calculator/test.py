import unittest
from calc import calculator
from exceptions import ZeroDivError, WrongInputError


class OperationsTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator('4+7'), 11)

    def test_subtract(self):
        self.assertEqual(calculator('10-5'), 5)

    def test_multiply(self):
        self.assertEqual(calculator('3*7'), 21)

    def test_divide(self):
        self.assertEqual(calculator('10/2'), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivError):
            calculator('10/0')

    def test_symbols(self):
        with self.assertRaises(WrongInputError):
            calculator('3%4')

    def test_no_sign(self):
        with self.assertRaises(WrongInputError):
            calculator('2 333')

    def test_one_integer(self):
        with self.assertRaises(WrongInputError):
            calculator('44/')

    def test_decimal(self):
        with self.assertRaises(WrongInputError):
            calculator('2.2+3')

    def test_len(self):
        with self.assertRaises(WrongInputError):
            calculator('2+2-1')

    def test_letters(self):
        with self.assertRaises(WrongInputError):
            calculator('2+b')


if __name__ == '__main__':
    unittest.main()