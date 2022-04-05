import sqlite3


class CalculatorDB:
    __conn = None

    def __init__(self, database, clear=False):
        self.__conn = sqlite3.connect(database)
        self.__check_bd()
        if clear:
            self.__clear_DB()

    def __check_bd(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS example(exampleInput text, exampleOutput text)')
            self.__conn.commit()
        except Exception:
            raise TypeError

    def add_example(self, exampleInput, exampleOutput):
        if not isinstance(exampleInput, str) or not isinstance(exampleOutput, str):
            raise ValueError
        try:
            cursor = self.__conn.cursor()
            cursor.execute('INSERT INTO example(exampleInput, exampleOutput) VALUES(?, ?)',
                           [exampleInput, exampleOutput])
            self.__conn.commit()
            return True
        except Exception:
            raise TypeError

    def get_all_examples(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute('SELECT * FROM example WHERE 1')
            return cursor.fetchall()
        except Exception:
            raise TypeError

    def __clear_DB(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute('DELETE FROM example')
            self.__conn.commit()
        except Exception:
            raise TypeError
