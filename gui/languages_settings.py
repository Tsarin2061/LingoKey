import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QDialog, QComboBox, QSizePolicy, QMessageBox
from .languages import get_lang_code_by_name, languages
from .button import Button
from config import config
from handlers import add_hot_key_to_translator

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle('Adding a language')
        self.initUI()

    def initUI(self):
        # Text fields for entering data
        self.from_lang = self.create_combo_box("en")
        self.to_lang = self.create_combo_box("uk")
        self.hot_key = QLineEdit(self)
        self.hot_key.setPlaceholderText("Enter hot key")

        # Button to confirm input
        okButton = Button("Save", self)
        okButton.clicked.connect(self.save)

        # Розташування компонентів у діалоговому вікні
        layout = QVBoxLayout()
        layout.addWidget(self.from_lang)
        layout.addWidget(self.to_lang)
        layout.addWidget(okButton)
        self.setLayout(layout)

    def save(self):
        if self.hot_key.text() == "":
            self.parent.showError("Enter hot key")
        else:
            self.accept()
    def getInputs(self):
        from_lang = get_lang_code_by_name(self.from_lang.currentText())
        to_lang = get_lang_code_by_name(self.to_lang.currentText())
        hot_key = self.hot_key.text()
        item_to_config = {
            "from_language": from_lang,
            "to_language": to_lang,
            "hot_key": hot_key
        }
        config["languages"].append(item_to_config)
        config.save()
        add_hot_key_to_translator(item_to_config)
        return from_lang, to_lang, hot_key

    def create_combo_box(self, current_text):
        combo_box = QComboBox(self)
        combo_box.addItems(list(languages.values()))
        combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        combo_box.setCurrentText(current_text)
        return combo_box


class MainWindow(QWidget):
    def __init__(self, abbreviations_window=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Створення таблиці
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        for item in config["languages"]:
            self.addRow((item["from_language"], item["to_language"], item["hot_key"]))
        self.table.setHorizontalHeaderLabels(["From", "To", "Hot key"])

        # Кнопка для відкриття вікна введення
        inputButton = Button("Add language", self)
        inputButton.clicked.connect(self.openInputDialog)

        # Розташування таблиці та кнопки у віджеті
        layout = QVBoxLayout()
        layout.addWidget(inputButton)
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Налаштування вікна
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Головне вікно')

    def openInputDialog(self):
        dialog = InputDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            inputs = dialog.getInputs()
            self.addRow(inputs)

    def addRow(self, inputs):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(inputs[0]))
        self.table.setItem(row_count, 1, QTableWidgetItem(inputs[1]))
        self.table.setItem(row_count, 2, QTableWidgetItem(inputs[2]))

    def showError(self, text):
        # Створення та налаштування вікна з помилкою
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        # msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        # msg.setDetailedText("Тут ви можете додати детальний опис помилки.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  # Відображення вікна
