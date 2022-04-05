import unittest

from main import Calculator


class Empty(unittest.TestCase):
    def test_empty(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string(""))

    def test_empty_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string(""), int))

    def test_empty_with_space(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string(" "))

    def test_empty_with_space_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string(" "), int))

    def test_empty_with_spaces(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string("    "))

    def test_empty_with_spaces_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("   "), int))

    def test_empty_none(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string(None)


class Number(unittest.TestCase):
    def test_number_int(self):
        calc = Calculator()
        self.assertEqual(124, calc.calculate_reverse_polish_string("124"))

    def test_number_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("124"), int))

    def test_number_neg_int(self):
        calc = Calculator()
        self.assertEqual(-124, calc.calculate_reverse_polish_string("-124"))

    def test_number_big_int(self):
        calc = Calculator()
        self.assertEqual(12412431223123155351351351325, calc.calculate_reverse_polish_string("12412431223123155351351351325"))

    def test_number_big_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("12412431223123155351351351325"), int))

    def test_number_big_float(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string("1241243121241352312.315534123551351351325124")

    def test_number_float(self):
        calc = Calculator()
        self.assertEqual(124.25, calc.calculate_reverse_polish_string("124.25"))

    def test_number_float_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("124.25"), float))

    def test_number_float_with_dots(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string("124.25.1")

    def test_number_hex(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string(f"{hex(25)}")

    def test_number_bin(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string(f"{bin(25)}")

    def test_number_string(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string("acs")

    def test_number_list(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string([])

    def test_number_tuple(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string(())

    def test_number_number(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string(213)


class Add(unittest.TestCase):
    def test_add_int_to_int(self):
        calc = Calculator()
        self.assertEqual(2, calc.calculate_reverse_polish_string("1 1 +"))

    def test_add_int_to_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1 1 +"), int))

    def test_add_zero_to_zero(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string("0 0 +"))

    def test_add_zero_to_zero_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1 1 +"), int))

    def test_add_float_to_int(self):
        calc = Calculator()
        self.assertEqual(2.5, calc.calculate_reverse_polish_string("1.5 1 +"))

    def test_add_float_to_int_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 1 +"), float))

    def test_add_float_to_float(self):
        calc = Calculator()
        self.assertEqual(4.1, calc.calculate_reverse_polish_string("1.5 2.6 +"))

    def test_add_float_to_float_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 2.6 +"), float))

    def test_add_float_to_float_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 2.5 +"), int))


class Minus(unittest.TestCase):
    def test_minus_int_to_int(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string("1 1 -"))

    def test_add_int_to_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1 1 -"), int))

    def test_minus_zero_to_zero(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string("0 0 -"))

    def test_minus_zero_to_zero_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("0 0 -"), int))

    def test_minus_float_to_int(self):
        calc = Calculator()
        self.assertEqual(0.5, calc.calculate_reverse_polish_string("1.5 1 -"))

    def test_minus_float_to_int_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 1 -"), float))

    def test_minus_float_to_float(self):
        calc = Calculator()
        self.assertEqual(-1.1, calc.calculate_reverse_polish_string("1.5 2.6 -"))

    def test_minus_float_to_float_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 2.6 -"), float))

    def test_minus_float_to_float_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 2.5 -"), int))


class Multiply(unittest.TestCase):
    def test_multiply_int_to_int(self):
        calc = Calculator()
        self.assertEqual(4, calc.calculate_reverse_polish_string("2 2 *"))

    def test_multiply_int_to_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("2 2 *"), int))

    def test_multiply_zero_to_zero(self):
        calc = Calculator()
        self.assertEqual(0, calc.calculate_reverse_polish_string("0 0 *"))

    def test_multiply_zero_to_zero_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("0 0 *"), int))

    def test_multiply_float_to_int(self):
        calc = Calculator()
        self.assertEqual(4.5, calc.calculate_reverse_polish_string("1.5 3 *"))

    def test_multiply_float_to_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 2 *"), int))

    def test_multiply_float_to_int_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 3 *"), float))

    def test_multiply_float_to_float(self):
        calc = Calculator()
        self.assertEqual(3.9, calc.calculate_reverse_polish_string("1.5 2.6 *"))

    def test_multiply_float_to_float_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("1.5 2.6 *"), float))


class Divide(unittest.TestCase):
    def test_divide_int_to_int(self):
        calc = Calculator()
        self.assertEqual(2, calc.calculate_reverse_polish_string("4 2 /"))

    def test_divide_int_to_int_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("5 2 /"), float))

    def test_divide_int_to_int_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("4 2 /"), int))

    def test_divide_float_to_int(self):
        calc = Calculator()
        self.assertEqual(1.8, calc.calculate_reverse_polish_string("3.6 2 /"))

    def test_divide_float_to_int_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("3.6 2 /"), float))

    def test_divide_float_to_float(self):
        calc = Calculator()
        self.assertEqual(2, calc.calculate_reverse_polish_string("5.2 2.6 /"))

    def test_divide_float_to_float_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("5.5 2.6 /"), float))

    def test_divide_float_to_float_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("5.2 2.6 /"), int))

    def test_divide_number_to_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.calculate_reverse_polish_string("2 0 /")


class DifferentOperators(unittest.TestCase):
    def test_minus_and_plus(self):
        calc = Calculator()
        self.assertEqual(7, calc.calculate_reverse_polish_string("5 4 2 - +"))

    def test_minus_and_plus_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("5 4 2 - +"), int))

    def test_minus_and_plus_and_multiply(self):
        calc = Calculator()
        self.assertEqual(13, calc.calculate_reverse_polish_string("5 4 2 - 4 * +"))

    def test_minus_and_plus_and_multiply_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("5 4 2 - 4 * +"), int))

    def test_divide_and_multiply(self):
        calc = Calculator()
        self.assertEqual(10, calc.calculate_reverse_polish_string("5 4 2 * 4 / *"))

    def test_divide_and_multiply_type_int(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("5 4 2 * 4 / *"), int))

    def test_all_operators(self):
        calc = Calculator()
        self.assertEqual(-578.46022748, calc.calculate_reverse_polish_string("123 45 * 46 12 / 3 1 2 + / + 6 5 4 + + - * 88 / 66 + 55 11 / -"))

    def test_all_operators_type_float(self):
        calc = Calculator()
        self.assertTrue(isinstance(calc.calculate_reverse_polish_string("123 45 * 46 12 / 3 1 2 + / + 6 5 4 + + - * 88 / 66 + 55 11 / -"), float))


class OperatorsWithOutSpaces(unittest.TestCase):
    def test_operator_without_left_space(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string("2 0/")

    def test_operator_without_right_space(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string("2 0 /2 +")

    def test_operator_without_spaces(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.calculate_reverse_polish_string("2 0/2 +")


class OperatorsErrors(unittest.TestCase):
    def test_operator_error_only_operator_plus(self):
        calc = Calculator()
        with self.assertRaises(Exception):
            calc.calculate_reverse_polish_string("+")

    def test_operator_error_only_operator_multiply(self):
        calc = Calculator()
        with self.assertRaises(Exception):
            calc.calculate_reverse_polish_string(" *")

    def test_operator_error_many_operators(self):
        calc = Calculator()
        with self.assertRaises(Exception):
            calc.calculate_reverse_polish_string("2 2 + 2 * -")


if __name__ == '__main__':
    unittest.main()


