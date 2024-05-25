# -*- coding: utf-8 -*-
import time
import logging
import sys
import keyboard
from PyQt5.QtWidgets import QApplication
from gui import AbbreviationsWindow, MainWindow
from helper import get_clipboard, past_into_clipboard
from translator import Translator
from config import config
from abbreviation_handler import load_abbreviation
from hot_keys_on_platforms import hot_keys_on_platform


logging.basicConfig(level=logging.DEBUG)

def translate():
    logging.debug("translate")
    time.sleep(0.2)
    keyboard.send(hot_keys_on_platform["copy"])
    time.sleep(0.1)
    text = get_clipboard()
    translator = Translator(
        config["from_language"], config["to_language"], text
    )
    translator.run()
    past_into_clipboard(translator.translation)
    time.sleep(0.1)
    keyboard.send(hot_keys_on_platform["paste"])

load_abbreviation()

app = QApplication(sys.argv)
abbreviations_window = AbbreviationsWindow()
main_window = MainWindow(abbreviations_window=abbreviations_window)
main_window.show()

keyboard.add_hotkey(hot_keys_on_platform["translate"], translate, timeout=2)

# I commented text below, becasuse I did not get the purpose of it
# function "open setting is also deleted"
# keyboard.add_hotkey('cmd+m', open_settings, timeout=2)
# keyboard.wait()

sys.exit(app.exec_())
