from abc import ABC, abstractmethod


class Classe(ABC):
    @abstractmethod
    def get_name(self):
        pass