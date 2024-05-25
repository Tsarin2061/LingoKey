import logging
import json


spec = {
    "from_language": "auto",
    "to_language": "en",
    "abr": {}
}


class Config(dict):
    """
    A class that provides an interface for interacting with a configuration file
    # You can work with it like a regular dictionary
    """


    _FILE_NAME = "config.json"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            data = self._load()
        except:
            logging.debug("Doesn't exist config file")
            data = {}
        self.update({**spec, **data})

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save()

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save()

    def _save(self):
        file = open(self._FILE_NAME, "w")
        json.dump(self, file, indent=4,ensure_ascii=False)
        file.close()
        logging.debug("Saved config")

    def _load(self) -> dict:
        logging.debug("Loading config")
        file = open(self._FILE_NAME, "r")
        data = json.load(file)
        file.close()
        return data

        # Ваша додаткова функція
        print("Зміни у словнику виконано")

config = Config()