from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtCore import Qt
from languages import langcodes
from config import config
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Selector")

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create first combo box for languages
        self.combo_box1 = QComboBox(self)
        self.combo_box1.addItems(langcodes)
        self.combo_box1.setMaxVisibleItems(10)  # Set the maximum number of visible items
        self.combo_box1.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        self.combo_box1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.combo_box1.setCurrentText(config.get('from_language'))
        layout.addWidget(self.combo_box1)

        # Create second combo box for languages
        self.combo_box2 = QComboBox(self)
        self.combo_box2.addItems(langcodes)
        self.combo_box2.setMaxVisibleItems(10)  # Set the maximum number of visible items
        self.combo_box2.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        self.combo_box2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.combo_box1.setCurrentText(config.get('to_language'))

        layout.addWidget(self.combo_box2)

        # Create a button
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.on_submit)
        layout.addWidget(self.button)

    def on_submit(self):
        lang1 = self.combo_box1.currentText()
        lang2 = self.combo_box2.currentText()
        config.set(lang1, lang2)
        print(f"Selected languages: {lang1} and {lang2}")


