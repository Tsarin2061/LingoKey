import logging
import json


spec = {
    "from_language": "auto",
    "to_language": "en",
}


class Config:
    """
    A class that provides an interface for interacting with a configuration file
    For interaction, it is enough to use the get and set methods
    """

    _FILE_NAME = "config.json"

    def __init__(self):
        try:
            self.data = self._load()
        except:
            logging.debug("Doesn't exist config file")
            self.data = {}
        self.data = {**spec, **self.data}

    def get(self, key: str):
        logging.debug(f"Getting {key} from config")
        return self.data.get(key, None)

    def set(self, key: str, value: str):
        logging.debug(f"Setting {key} to {value} in config")
        self.data[key] = value
        self._save()

    def _save(self):
        file = open(self._FILE_NAME, "w")
        json.dump(self.data, file, indent=4)
        file.close()
        logging.debug("Saved config")

    def _load(self) -> dict:
        logging.debug("Loading config")
        file = open(self._FILE_NAME, "r")
        data = json.load(file)
        file.close()
        return data


config = Config()
