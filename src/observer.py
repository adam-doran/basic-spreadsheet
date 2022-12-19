from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self._observers = set()

    @abstractmethod
    def notify_observers(self):
        ...

    @abstractmethod
    def subscribe(self, observer):
        ...

    @abstractmethod
    def unsubscribe(self, observer):
        ...
