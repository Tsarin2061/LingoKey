import logging
import time
import keyboard
from config import config
from hot_keys_on_platforms import hot_keys_on_platform
from helper import get_clipboard, past_into_clipboard
from translator import Translator


logging.basicConfig(level=logging.DEBUG)


def translate(lang_item):
    logging.debug("translate")
    time.sleep(0.2)
    keyboard.send(hot_keys_on_platform["copy"])
    time.sleep(0.1)
    text = get_clipboard()
    translator = Translator(
        lang_from="auto",
        # lang_to=config["to_language"],
        lang_to=lang_item["to_language"],
        text=text,
        # lang_swap=config["from_language"]
        lang_swap=lang_item["from_language"],
    )
    translator.run()
    past_into_clipboard(translator.translation)
    time.sleep(0.1)
    keyboard.send(hot_keys_on_platform["paste"])


def load_abbreviation():
    for abr, text in config.get('abr').items():
        keyboard.add_abbreviation(abr, text)

def add_abbreviation(abbreviation, value):
    keyboard.add_abbreviation(abbreviation, value)    

def remove_abbreviation(abbreviation):
    keyboard.remove_abbreviation(abbreviation)


def load_hot_keys():
    for item in config["languages"]:
        keyboard.add_hotkey(item["hot_key"], translate, timeout=2, args=[item])

def add_hot_key_to_translator(item):
    keyboard.add_hotkey(item["hot_key"], translate, timeout=2, args=[item])