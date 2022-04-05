import pytest
from GUI import Ui_Dialog


@pytest.fixture
def app(qtbot):
    test_hello_app = Ui_Dialog()
    qtbot.addWidget(test_hello_app)
    return test_hello_app


def test_solve_correct_example(app):
    app.exampleTextEdit.setText("1 2 +")
    app.solveButton.click()
    assert "3" == app.answerTextBrowser.toPlainText()


def test_solve_empty_example(app):
    app.exampleTextEdit.setText("")
    app.solveButton.click()
    assert "0" == app.answerTextBrowser.toPlainText()


def test_solve_incorrect_example(app):
    app.exampleTextEdit.setText("1 2 + 2")
    app.solveButton.click()
    assert "Error" == app.answerTextBrowser.toPlainText()


def test_save_correct_example(app):
    app.exampleTextEdit.setText("1 2 +")
    app.solveButton.click()
    app.saveButton.click()
    save = app.historyTextBrowser.toPlainText()
    assert "1) 1 2 + = 3\n" == save


def test_save_incorrect_example(app):
    app.exampleTextEdit.setText("1 2 + 2")
    app.solveButton.click()
    app.saveButton.click()
    save = app.historyTextBrowser.toPlainText()
    assert "1) 1 2 + 2 = Error\n" == save


def test_save_examples(app):
    app.exampleTextEdit.setText("1 2 + 2")
    app.solveButton.click()
    app.saveButton.click()
    app.exampleTextEdit.setText("1 2 + 2")
    app.solveButton.click()
    app.saveButton.click()
    app.exampleTextEdit.setText("1 2 + 2 * 6 +")
    app.solveButton.click()
    app.saveButton.click()
    save = app.historyTextBrowser.toPlainText()
    assert "1) 1 2 + 2 = Error\n2) 1 2 + 2 = Error\n3) 1 2 + 2 * 6 + = 12\n" == save


def test_save_empty_example(app):
    app.exampleTextEdit.setText("")
    app.solveButton.click()
    app.saveButton.click()
    save = app.historyTextBrowser.toPlainText()
    assert "" == save


def test_save_empty_answer(app):
    app.exampleTextEdit.setText("1 2 +")
    app.saveButton.click()
    save = app.historyTextBrowser.toPlainText()
    assert "" == save


def test_save_empty_example_and_answer(app):
    app.exampleTextEdit.setText("")
    app.saveButton.click()
    save = app.historyTextBrowser.toPlainText()
    assert "" == save


def test_answer_solve_and_change_example(app):
    app.exampleTextEdit.setText("1 2 +")
    app.solveButton.click()
    app.exampleTextEdit.setText("1 2 ")
    assert "" == app.answerTextBrowser.toPlainText()
