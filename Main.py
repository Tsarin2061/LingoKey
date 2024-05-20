import time
import logging
import keyboard
import sys
from PyQt5.QtWidgets import QApplication
from gui.main import MainWindow
from helper import get_clipboard, past_into_clipboard
from translator import Translator
from config import config
from gui.languages import langcodes
from hot_keys_on_platforms import hot_keys_on_platform


logging.basicConfig(level=logging.DEBUG)


def translate():
    logging.debug("translate")
    keyboard.send(hot_keys_on_platform["copy"])
    time.sleep(0.1)
    text = get_clipboard()
    translator = Translator(
        config.get("from_language"), config.get("to_language"), text
    )
    translator.run()
    past_into_clipboard(translator.translation)
    keyboard.send(hot_keys_on_platform["paste"])

app = QApplication(sys.argv)
main_window = MainWindow(langcodes = langcodes, config = config)
main_window.show()

keyboard.add_hotkey(hot_keys_on_platform["translate"], translate, timeout=2)

# I commented text below, becasuse I did not get the purpose of it
# function "open setting is also deleted"
# keyboard.add_hotkey('cmd+m', open_settings, timeout=2)
# keyboard.wait()

sys.exit(app.exec_())