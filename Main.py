from pynput.keyboard import Listener
from keyboard_handler import Keyboard
from helper import get_clipboard, simulate_ctrl_c, past_into_clipboard, paste_text
from translator import Translator
from PyQt5.QtWidgets import QApplication
from gui.main import app
from config import config
import sys


def translate():
    simulate_ctrl_c()
    text = get_clipboard()
    translator = Translator(lang_from=config.get('from_language'), lang_to=config.get('to_language'), text=text)
    translator.run()
    text = translator.translation + " "

    past_into_clipboard(text)
    paste_text()

keyboard = Keyboard(translate)

try:
    with Listener(
        on_press=keyboard.on_press, on_release=keyboard.on_release
    ) as listener:
        listener.join()
except KeyboardInterrupt:
    exit(0)
