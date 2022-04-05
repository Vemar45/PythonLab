import sys
from PyQt5 import QtWidgets
from GUI import Ui_Dialog
from main import Calculator
from CaclulatorDB import CalculatorDB


class CalculatorGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalculatorGUI, self).__init__()
        self.calculator = Calculator()
        self.historyDB = CalculatorDB("history.db", True)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.solveButton.clicked.connect(self.__solve_button_click)
        self.ui.exampleTextEdit.textChanged.connect(self.__example_text_edit_changed_text)
        self.ui.saveButton.clicked.connect(self.__save_button_click)

    def __example_text_edit_changed_text(self):
        self.__set_example_result("")

    def __solve_button_click(self):
        example = self.ui.exampleTextEdit.toPlainText()
        try:
            result = self.calculator.calculate_reverse_polish_string(example)
            self.__set_example_result(result)
        except Exception:
            self.__set_example_result("Error")

    def __set_example_result(self, result):
        self.ui.answerTextBrowser.setText(str(result))

    def __save_button_click(self):
        example = self.ui.exampleTextEdit.toPlainText()
        result = self.ui.answerTextBrowser.toPlainText()
        if len(example.split()) > 0 and len(result.split()) > 0:
            self.historyDB.add_example(example, result)
            self.__update_history()

    def __update_history(self):
        examples = self.historyDB.get_all_examples()
        text = ""
        for idx, example in enumerate(examples):
            text += f'{idx + 1}) {example[0]} = {example[1]}\n'
        self.ui.historyTextBrowser.setText(text)


app = QtWidgets.QApplication([])
application = CalculatorGUI()
application.show()
sys.exit(app.exec())
