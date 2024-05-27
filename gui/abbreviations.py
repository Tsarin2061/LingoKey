import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QComboBox,
    QHBoxLayout,
    QScrollArea,
    QSizePolicy,
)
from .custom_widgets import Button
import logging
from config import config
from handlers import load_abbreviation, add_abbreviation, remove_abbreviation

class AbbreviationsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.update_window()

    def init_ui(self):
        self.setWindowTitle("LingoKey")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")

        # Central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Scroll area for existing abbreviations
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll_area)

        # Entry section for new abbreviation
        self.entry_layout = QHBoxLayout()
        self.abbreviation_input = QLineEdit()
        self.abbreviation_input.setPlaceholderText("Enter abbreviation")
        self.abbreviation_input.setStyleSheet(
            "background-color: #FFFFFF; color: #000000;"
        )

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter text")
        self.text_input.setStyleSheet("background-color: #FFFFFF; color: #000000;")

        self.add_button = Button("Add")
        self.add_button.clicked.connect(self.set_abbreviations)

        self.entry_layout.addWidget(self.abbreviation_input)
        self.entry_layout.addWidget(self.text_input)
        self.entry_layout.addWidget(self.add_button)

        self.main_layout.addLayout(self.entry_layout)

        # Initialize rows container
        self.rows = []

    def create_row_widget(self, abbreviation, text):
        abbreviation_display = QLineEdit()
        abbreviation_display.setText(abbreviation)
        abbreviation_display.setReadOnly(True)
        abbreviation_display.setStyleSheet("background-color: #FFFFFF; color: #000000;")

        text_display = QLineEdit()
        text_display.setText(text)
        text_display.setReadOnly(True)
        text_display.setStyleSheet("background-color: #FFFFFF; color: #000000;")

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)

        row_layout.addWidget(abbreviation_display)
        row_layout.addWidget(text_display)

        delete_button = Button("Delete")
        delete_button.clicked.connect(lambda: self.delete_row(row_widget, abbreviation))
        row_layout.addWidget(delete_button)

        return row_widget

    def set_abbreviations(self, abbreviation):
        abbreviation = self.abbreviation_input.text()
        text = self.text_input.text()
        if abbreviation and text:
            config["abr"][abbreviation] = text
            config.save()
            add_abbreviation(abbreviation, text)
            self.abbreviation_input.clear()
            self.text_input.clear()
            self.update_window()  # Call the update_window method after initializing UI

    def update_window(self):
        # Clear existing rows
        for i in reversed(range(self.scroll_layout.count())):
            widget_to_remove = self.scroll_layout.itemAt(i).widget()
            self.scroll_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

        # Read from config and add new rows
        for abr, txt in config["abr"].items():
            row_widget = self.create_row_widget(abr, txt)
            self.scroll_layout.addWidget(row_widget)
            self.rows.append(row_widget)

            self.scroll_layout.addWidget(row_widget)
            self.rows.append(row_widget)
        

    def delete_row(self, row_widget, abbreviation):
        self.scroll_layout.removeWidget(row_widget)
        self.rows.remove(row_widget)
        row_widget.setParent(None)  # Remove the widget from the layout and delete it

        # Also remove the abbreviation from the config
        if abbreviation in config["abr"]:
            del config["abr"][abbreviation]
            config.save()
            remove_abbreviation(abbreviation)
