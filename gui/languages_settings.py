from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QDialog, QComboBox, QSizePolicy, QMessageBox
from .languages import get_lang_code_by_name, languages
from .custom_widgets import Button, TableWidget
from config import config
from handlers import add_hot_key_to_translator
from utilities import is_exists_language_configuration, is_hot_key_in_list_languages

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

        # Positioning components in a dialog box
        layout = QVBoxLayout()
        layout.addWidget(self.from_lang)
        layout.addWidget(self.to_lang)
        layout.addWidget(okButton)
        self.setLayout(layout)

    def save(self):
        from_lang, to_lang, hot_key = self.getInputs()
        if hot_key == "":
            self.parent.showError("Enter hot key")
        elif is_exists_language_configuration(from_lang, to_lang, hot_key):
            self.parent.showError("Language configuration already exists", "Warning", QMessageBox.Warning) 
        elif is_hot_key_in_list_languages(hot_key):
            self.parent.showError("Hot key already exists", "Warning", QMessageBox.Warning)
        else:
            try:
                add_hot_key_to_translator(item_to_config)
            except Exception as e:
                self.parent.showError("Failed to add hot key", "Error", QMessageBox.Critical)
                return False
            item_to_config = {
                "from_language": from_lang,
                "to_language": to_lang,
                "hot_key": hot_key
            }
            config["languages"].append(item_to_config)
            config.save()
            self.accept()
    
    def getInputs(self):
        from_lang = get_lang_code_by_name(self.from_lang.currentText())
        to_lang = get_lang_code_by_name(self.to_lang.currentText())
        hot_key = self.hot_key.text()
        return from_lang, to_lang, hot_key

    def create_combo_box(self, current_text):
        combo_box = QComboBox(self)
        combo_box.addItems(list(languages.values()))
        combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        combo_box.setCurrentText(current_text)
        return combo_box


class LanguagesWindow(QWidget):
    def __init__(self, abbreviations_window=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Button to open the input window
        self.inputButton = Button("Add language", self)
        self.inputButton.clicked.connect(self.openInputDialog)
        
        # Creating a table
        self.table = TableWidget(self)
        self.table.setColumnCount(3)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        for item in config["languages"]:
            self.addRow((item["from_language"], item["to_language"], item["hot_key"]))
        self.table.setHorizontalHeaderLabels(["From", "To", "Hot key"])

        # Button to delete table row
        self.delete_button = Button("Delete", self)
        self.delete_button.clicked.connect(self.delete_row)

        # Placement of the table and buttons in the widget
        layout = QVBoxLayout()
        layout.addWidget(self.inputButton)
        layout.addWidget(self.table)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

        # Window settings
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('LingoKey')

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

    def delete_row(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            rowData = []
            for column in range(self.table.columnCount()):
                item = self.table.item(selected_row, column)
                if item is not None:
                    rowData.append(item.text())
                else:
                    rowData.append(None)
            self.delete_lang_from_config(rowData)
            self.table.removeRow(selected_row)

    def delete_lang_from_config(self, data: list):
        for item in config["languages"]:
            if item["from_language"] == data[0] and item["to_language"] == data[1] and item["hot_key"] == data[2]:
                config["languages"].remove(item)
                config.save()
                break

    def showError(self, text: str, title: str = "Error", icon = QMessageBox.Critical):
        # Створення та налаштування вікна з помилкою
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        # msg.setInformativeText(text)
        msg.setWindowTitle(title)
        # msg.setDetailedText("Тут ви можете додати детальний опис помилки.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  # Відображення вікна
