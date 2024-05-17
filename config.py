import json


spec = {
    "from_language": "auto",
    "to_language": "en",
}

class Config:
    """
    Клас, який забезпечує інтерфейс для взаємодії з файлом конфігурації
    Для взаємодії достатньо використовувати метод get і set
    """
    
    _FILE_NAME = "config.json"
    def __init__(self):
        try:
            self.data = self._load()        
        except:
            self.data = spec

    def get(self, key: str):
        return self.data.get(key, None)

    def set(self, key: str, value: str):
        self.data[key] = value
        self._save()

    def _save(self):
        file = open(self._FILE_NAME, "w")
        json.dump(self.data, file, indent=4)
        file.close()

    def _load(self) -> dict:
        file = open(self._FILE_NAME, "r")
        data = json.load(file)
        file.close()
        return data

config = Config()