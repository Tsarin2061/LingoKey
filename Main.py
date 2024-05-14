import time
from pynput.keyboard import Listener
from keyboard_handler import Keyboard
from helper import get_clipboard, simulate_ctrl_c, past_into_clipboard,simulate_ctrl_v
from deep_translator import GoogleTranslator
from translator import Translator



def translate():
    simulate_ctrl_c()
    text = get_clipboard()
    # There is going to be translator
    # translated = GoogleTranslator(source='auto', target='en').translate(text)
    translator = Translator("auto", "en", text)
    translator.run( )
    from threading import Timer
    Timer(1, simulate_ctrl_v, translator.translation).start()
    # simulate_ctrl_v()

keyboard = Keyboard(translate)

try:
    with Listener(on_press=keyboard.on_press, on_release=keyboard.on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    exit(0)