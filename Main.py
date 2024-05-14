from pynput.keyboard import Listener
from keyboard import Keyboard
from helper import get_clipboard, simulate_ctrl_c, past_into_clipboard,paste_text
from translator import Translator

def translate():
    print("Hello")
    # paste_text("Text message")
    # return
    simulate_ctrl_c()
    text = get_clipboard()
    print(f"З буфера обміну отримано {text}")
    translator = Translator("auto", "en", text)
    print(f"Запускаємо перекладач з текстом {text}")
    translator.run()
    # There is going to be translator 
    # past_into_clipboard(text)
    paste_text(translator.translation)


keyboard = Keyboard(translate)


try:
    with Listener(on_press=keyboard.on_press, on_release=keyboard.on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    exit(0)