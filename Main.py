import time
import keyboard
from helper import get_clipboard, past_into_clipboard
from translator import Translator

def translate():
    keyboard.send('ctrl+с')
    time.sleep(0.1)
    # keyboard.send('ctrl+с')
    text = get_clipboard()
    translator = Translator("auto", "en", text)
    translator.run()
    past_into_clipboard(translator.translation)
    # time.sleep(0.1)
    keyboard.send('ctrl+v')


keyboard.add_hotkey('ctrl+shift+w', translate, timeout=2)
keyboard.add_hotkey('cmd+shift+w', translate, timeout=2)
keyboard.wait()