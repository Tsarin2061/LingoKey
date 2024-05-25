import keyboard
from config import config

def abbreviation_handler():
    abr_text = config.get('abr')
    for abr, text in abr_text.items():
        keyboard.add_abbreviation(abr, text)



