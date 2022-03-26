from collections import deque


class Calculator:
    operators = ("+", "-", "/", "*")

    @staticmethod
    def __get_number_from_str(string):
        try:
            number = float(string)
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            return None

    @staticmethod
    def __calculate(value1: float, value2: float, operator: str) -> float:
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        elif operator == "/":
            return value1 / value2
        raise ValueError

    def calculate_reverse_polish_string(self, reversePolishStr: str):
        if not isinstance(reversePolishStr, str):
            raise ValueError
        values = deque()
        objs = reversePolishStr.split()
        if len(objs) <= 0:
            return 0
        for obj in objs:
            value = Calculator.__get_number_from_str(obj)
            if value is not None:
                values.append(value)
                continue
            if obj in self.operators:
                if len(values) > 1:
                    value2, value1 = values.pop(), values.pop()
                    values.append(round(Calculator.__calculate(value1, value2, obj), 8))
            else:
                raise ValueError
        if len(values) == 1:
            return Calculator.__get_number_from_str(values.pop())
        else:
            raise Exception
