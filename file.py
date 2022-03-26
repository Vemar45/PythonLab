from collections import deque


class Calculator:

    @staticmethod
    def get_number_from_str(string: str):
        try:
            number = float(string)
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            return None

    @staticmethod
    def calculate(value1: float, value2: float, operator: str) -> float:
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        elif operator == "/":
            return value1 / value2
        raise ValueError


operators = ("+", "-", "/", "*")


def calc(reversePolishStr: str):
    if not isinstance(reversePolishStr, str):
        raise ValueError
    values = deque()
    objs = reversePolishStr.split()
    if len(objs) <= 0:
        return 0
    for obj in objs:
        value = Calculator.get_number_from_str(obj)
        if value is not None:
            values.append(value)
            continue
        if obj in operators:
            if len(values) > 1:
                value2, value1 = values.pop(), values.pop()
                values.append(round(Calculator.calculate(value1, value2, obj), 8))
    if len(values) == 1:
        return values.pop()
    else:
        raise Exception
