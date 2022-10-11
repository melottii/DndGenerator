from abc import ABC, abstractmethod


class Raca(ABC):
    @abstractmethod
    def get_name(self):
        pass
