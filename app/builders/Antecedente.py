from abc import ABC, abstractmethod


class Antecedente(ABC):
    @abstractmethod
    def __get_name__(self, personagem):
        pass

    @abstractmethod
    def __get_type__(self, personagem):
        pass

    @abstractmethod
    def __get_personalityTrait__(self, personagem):
        pass

    @abstractmethod
    def __get_ideal__(self, personagem):
        pass

    @abstractmethod
    def __get_bond__(self, personagem):
        pass

    @abstractmethod
    def __get_flaw__(self, personagem):
        pass
