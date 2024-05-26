# -*- coding: utf-8 -*-
import logging
import sys
from PyQt5.QtWidgets import QApplication
from gui import AbbreviationsWindow, MainWindow
from config import config
from handlers import load_abbreviation, load_hot_keys


logging.basicConfig(level=logging.DEBUG)


load_abbreviation()
load_hot_keys()

app = QApplication(sys.argv)
abbreviations_window = AbbreviationsWindow()
main_window = MainWindow(abbreviations_window=abbreviations_window)
main_window.show()

# keyboard.add_hotkey(hot_keys_on_platform["translate"], translate, timeout=2)

sys.exit(app.exec_())
