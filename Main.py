import time
from pynput.keyboard import Listener
from keyboard_handler import Keyboard
from helper import get_clipboard, simulate_ctrl_c, past_into_clipboard,simulate_ctrl_v
from deep_translator import GoogleTranslator



def translate():
    simulate_ctrl_c()
    text = get_clipboard()
    # There is going to be translator
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    simulate_ctrl_v(translated)

keyboard = Keyboard(translate)

try:
    with Listener(on_press=keyboard.on_press, on_release=keyboard.on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    exit(0)