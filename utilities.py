from config import config


def is_exists_language_configuration(from_lang: str, to_lang: str, hot_key: str) -> bool:
    for item in config["languages"]:
        if item["from_language"] == from_lang and item["to_language"] == to_lang and item["hot_key"] == hot_key:
            return True
    return False


def is_hot_key_in_list_languages(hot_key: str) -> bool:
    for item in config["languages"]:
        if item["hot_key"] == hot_key:
            return True
    return False