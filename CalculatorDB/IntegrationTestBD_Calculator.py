import unittest
from CalculatorDB.CaclulatorDB import CalculatorDB


class Add(unittest.TestCase):
    def setUp(self):
        try:
            self.db = CalculatorDB(database="test.db", clear=True)
        except Exception:
            self.skipTest("Database not found")

    def test_add_example_str_str(self):
        self.assertTrue(self.db.add_example("1 2 +", "3"))

    def test_add_example_str_int(self):
        with self.assertRaises(ValueError):
            self.db.add_example("1 2 +", 3)

    def test_add_example_str_float(self):
        with self.assertRaises(ValueError):
            self.db.add_example("1 2 +", 3.4)

    def test_add_example_list_int(self):
        with self.assertRaises(ValueError):
            self.db.add_example("1 2 +", [3, 3])

    def test_add_example_str_tuple(self):
        with self.assertRaises(ValueError):
            self.db.add_example("1 2 +", (3, 3))

    def test_add_example_str_none(self):
        with self.assertRaises(ValueError):
            self.db.add_example("1 2 +", None)


class Contains(unittest.TestCase):
    def setUp(self):
        try:
            self.db = CalculatorDB(database="test.db", clear=True)
        except:
            self.skipTest("Database not found")

    def test_contains_example_1(self):
        self.db.add_example("1 2 +", "3")
        examples = self.db.get_all_examples()
        contains = False
        for example in examples:
            if example[0] == "1 2 +" and example[1] == "3":
                contains = True
                break
        self.assertTrue(contains)

    def test_contains_example_many(self):
        examples = [["1 2 +", "3"], ["1 3 +", "4"], ["1 4 +", "5"]]
        contains_arr = [False, False, False]
        self.db.add_example(examples[0][0], examples[0][1])
        self.db.add_example(examples[1][0], examples[1][1])
        self.db.add_example(examples[2][0], examples[2][1])
        db_examples = self.db.get_all_examples()
        for example in db_examples:
            for i in range(3):
                if example[0] == examples[i][0] and example[1] == examples[i][1]:
                    contains_arr[i] = True
                    break
        contains = contains_arr[0] and contains_arr[1] and contains_arr[2]
        self.assertTrue(contains)
