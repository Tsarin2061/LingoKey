import logging
import json


spec = {
    "abr": {},
    "languages": []
}


class Config(dict):
    """
    A class that provides an interface for interacting with a configuration file
    You can work with it like a regular dictionary
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

    def save(self):
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


config = Config()