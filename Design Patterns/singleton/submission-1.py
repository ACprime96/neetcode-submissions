import threading

class Singleton:
    lock = threading.Lock()
    instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        with cls.lock:
            if instance is None:
                cls.instance = super().__new__(cls)
                cls.instance.value = None
        return cls.instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
