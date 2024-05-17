import logging
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtCore import Qt
from config import config
from .languages import langcodes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Selector")

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create first combo box for languages
        self.from_lang_combo_box = QComboBox(self)
        self.from_lang_combo_box.addItems(langcodes)
        self.from_lang_combo_box.setMaxVisibleItems(10)  # Set the maximum number of visible items
        self.from_lang_combo_box.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        self.from_lang_combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.from_lang_combo_box.setCurrentText(config.get('from_language'))
        layout.addWidget(self.from_lang_combo_box)

        # Create second combo box for languages
        self.to_lang_combo_box = QComboBox(self)
        self.to_lang_combo_box.addItems(langcodes)
        self.to_lang_combo_box.setMaxVisibleItems(10)  # Set the maximum number of visible items
        self.to_lang_combo_box.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        self.to_lang_combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.from_lang_combo_box.setCurrentText(config.get('to_language'))

        layout.addWidget(self.to_lang_combo_box)

        # Create a button
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.on_submit)
        layout.addWidget(self.button)
        self.raise_()

    def on_submit(self):
        logging.debug("Saving settings")
        lang1 = self.from_lang_combo_box.currentText()
        lang2 = self.to_lang_combo_box.currentText()
        config.set("from_language", lang1)
        config.set("to_language", lang2)
        logging.debug(f"Selected languages: {self.from_lang_combo_box.currentText()} and {self.to_lang_combo_box.currentText()}")


