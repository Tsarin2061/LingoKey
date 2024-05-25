import keyboard
from config import config

def load_abbreviation():
    for abr, text in config.get('abr').items():
        keyboard.add_abbreviation(abr, text)

def add_abbreviation(abbreviation, value):
    keyboard.add_abbreviation(abbreviation, value)    

def remove_abbreviation(abbreviation):
    keyboard.remove_abbreviation(abbreviation)
