import time
import logging
import keyboard
from PyQt5.QtWidgets import QApplication
from gui.main import MainWindow
from helper import get_clipboard, past_into_clipboard
from translator import Translator
from config import config
from hot_keys_on_platforms import hot_keys_on_platform


logging.basicConfig(level=logging.DEBUG)


def translate():
    logging.debug('translate')
    keyboard.send(hot_keys_on_platform["copy"])
    time.sleep(0.05)
    text = get_clipboard()
    translator = Translator(config.get("from_language"), config.get("to_language"), text)
    translator.run()
    past_into_clipboard(translator.translation)
    keyboard.send(hot_keys_on_platform["paste"])

import sys
app = QApplication(sys.argv)
main_window = MainWindow()
def open_settings():
    main_window.show()
    logging.debug('open_settings')


keyboard.add_hotkey(hot_keys_on_platform["translate"], translate, timeout=2)
keyboard.add_hotkey('ctrl+alt+s', open_settings, timeout=2)
keyboard.wait()