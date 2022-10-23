from abc import ABC, abstractmethod


class Classe(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_name(self):
        pass
