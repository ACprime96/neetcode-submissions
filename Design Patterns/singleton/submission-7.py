import threading
class Singleton:
    _lock = threading.Lock()
    _instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
