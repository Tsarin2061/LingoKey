import logging
from PyQt5.QtWidgets import (
    QComboBox,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from .languages import get_lang_code_by_name, languages


class MainWindow(QMainWindow):
    CONFIG_FROM_LANGUAGE = "from_language"
    CONFIG_TO_LANGUAGE = "to_language"
    FIXED_WIDTH = 200
    FIXED_HEIGHT = 200
    STYLE_SHEET = """
    CustomTitleBar {
            background-color: #4B4B4B;
            color: #FFFFFF;
    }
    QMainWindow {
        background-color: #2E2E2E;  /* Set background color */
        color: #FFFFFF;  /* Set text color */
        border: 1px solid #333333;  /* Set border color */
    }
    QComboBox {
        background-color: #4B4B4B;
        color: #FFFFFF;
        border: 1px solid #555555;
        padding: 5px;
        border-radius: 3px;
    }
    QComboBox QAbstractItemView {
        background-color: #4B4B4B;
        color: #FFFFFF;
        selection-background-color: #5E5E5E;
    }
    QPushButton {
        background-color: #4B8F8C;
        color: #FFFFFF;
        border: 1px solid #4B8F8C;
        padding: 5px 10px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #77A1A0;
        border-color: #77A1A0;
    }
    QPushButton:pressed {
        background-color: #3A7B78;
        border-color: #3A7B78;
    }
    """

    def __init__(self, langcodes, config):
        super().__init__()
        self.langcodes = langcodes
        self.config = config

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LingoKey")
        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)
        self.setStyleSheet(self.STYLE_SHEET)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        from_lang = languages.get(self.config.get(self.CONFIG_FROM_LANGUAGE))
        self.from_lang_combo_box = self.create_combo_box(from_lang)
        layout.addWidget(self.from_lang_combo_box)

        to_lang = languages.get(self.config.get(self.CONFIG_TO_LANGUAGE))
        self.to_lang_combo_box = self.create_combo_box(to_lang)
        layout.addWidget(self.to_lang_combo_box)

        self.button = self.create_button("Save", self.on_submit)
        layout.addWidget(self.button)

        self.shortcuts_enabled = True

    def create_combo_box(self, current_text):
        combo_box = QComboBox(self)
        combo_box.addItems(list(languages.values()))
        combo_box.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        combo_box.setCurrentText(current_text)
        return combo_box

    def create_button(self, text, callback):
        button = QPushButton(text, self)
        button.clicked.connect(callback)
        return button

    def on_submit(self):
        logging.debug("Saving settings")
        from_lang = get_lang_code_by_name(self.from_lang_combo_box.currentText())
        to_lang = get_lang_code_by_name(self.to_lang_combo_box.currentText())
        self.config.set(self.CONFIG_FROM_LANGUAGE, from_lang)
        self.config.set(self.CONFIG_TO_LANGUAGE, to_lang)
        logging.debug(f"Selected languages: {from_lang} and {to_lang}")

