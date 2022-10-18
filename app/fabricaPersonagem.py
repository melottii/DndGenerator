from abc import ABC, abstractmethod

class personaInterface(ABC):

    @abstractmethod
    def get_classe(self, nome) -> dict:
        pass

    @abstractmethod
    def get_raca(self, nome) -> dict:
        pass
