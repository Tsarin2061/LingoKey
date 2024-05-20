import logging
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from PyQt5.QtCore import Qt
from config import config
from .languages import langcodes
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LingoKey")
        self.setStyleSheet(self.set_main_window_style())

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create "From" combo box for languages
        self.from_lang_combo_box = QComboBox(self)
        self.from_lang_combo_box.addItems(langcodes)
        self.from_lang_combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.from_lang_combo_box.setCurrentText(config.get("from_language"))
        layout.addWidget(self.from_lang_combo_box)

        # Create "To" combo box for languages
        self.to_lang_combo_box = QComboBox(self)
        self.to_lang_combo_box.addItems(langcodes)
        self.to_lang_combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.to_lang_combo_box.setCurrentText(config.get("to_language"))
        layout.addWidget(self.to_lang_combo_box)

        # probably this makes a big deal in shortcuts!
        self.shortcuts_enabled = True

        # Create a button
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.on_submit)
        layout.addWidget(self.button)
        self.raise_()

    def set_main_window_style(self):
        return """
        QMainWindow {
            background-color: #2E2E2E;  /* Set background color */
            color: #FFFFFF;  /* Set text color */
            border: 1px solid #333333;  /* Set border color */
        }
        """

    def on_submit(self):
        logging.debug("Saving settings")
        lang1 = self.from_lang_combo_box.currentText()
        lang2 = self.to_lang_combo_box.currentText()
        config.set("from_language", lang1)
        config.set("to_language", lang2)
        logging.debug(
            f"Selected languages: {self.from_lang_combo_box.currentText()} and {self.to_lang_combo_box.currentText()}"
        )
