import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication

from Calculator.ReversePolishCalculatorTest import Calculator
from CalculatorDB.CaclulatorDB import CalculatorDB


class Ui_Dialog(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.setEnabled(True)
        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 641, 121))
        self.groupBox.setObjectName("groupBox")
        self.saveButton = QtWidgets.QPushButton(self.groupBox)
        self.saveButton.setGeometry(QtCore.QRect(520, 70, 101, 41))
        self.saveButton.setObjectName("saveButton")
        self.answerTextBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.answerTextBrowser.setGeometry(QtCore.QRect(10, 70, 491, 41))
        self.answerTextBrowser.setObjectName("answerTextBrowser")
        self.exampleTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.exampleTextEdit.setGeometry(QtCore.QRect(10, 20, 491, 41))
        self.exampleTextEdit.setObjectName("exampleTextEdit")
        self.solveButton = QtWidgets.QPushButton(self.groupBox)
        self.solveButton.setGeometry(QtCore.QRect(520, 20, 101, 41))
        self.solveButton.setObjectName("solveButton")
        self.historyTextBrowser = QtWidgets.QTextBrowser(self)
        self.historyTextBrowser.setGeometry(QtCore.QRect(10, 120, 621, 341))
        self.historyTextBrowser.setObjectName("historyTextBrowser")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.saveButton.setText(_translate("Dialog", "Save"))
        self.solveButton.setText(_translate("Dialog", "Solve"))

        self.solveButton.clicked.connect(self.__solve_button_click)
        self.exampleTextEdit.textChanged.connect(self.__example_text_edit_changed_text)
        self.saveButton.clicked.connect(self.__save_button_click)

        self.calculator = Calculator()
        self.historyDB = CalculatorDB("history.db", True)

    def __example_text_edit_changed_text(self):
        self.__set_example_result("")

    def __solve_button_click(self):
        example = self.exampleTextEdit.toPlainText()
        try:
            result = self.calculator.calculate_reverse_polish_string(example)
            self.__set_example_result(result)
        except Exception:
            self.__set_example_result("Error")

    def __set_example_result(self, result):
        self.answerTextBrowser.setText(str(result))

    def __save_button_click(self):
        example = self.exampleTextEdit.toPlainText()
        result = self.answerTextBrowser.toPlainText()
        if len(example.split()) > 0 and len(result.split()) > 0:
            self.historyDB.add_example(example, result)
            self.__update_history()

    def __update_history(self):
        examples = self.historyDB.get_all_examples()
        text = ""
        for idx, example in enumerate(examples):
            text += f'{idx + 1}) {" ".join(example[0].split())} = {" ".join(example[1].split())}\n'
        self.historyTextBrowser.setText(text)


#app = QApplication(sys.argv)
#ex = Ui_Dialog()
#ex.show()
#sys.exit(app.exec_())