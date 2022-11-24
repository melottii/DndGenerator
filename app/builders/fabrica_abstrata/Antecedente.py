from abc import ABC, abstractmethod


class Antecedente(ABC):
    @abstractmethod
    def __get_name__(self):
        pass

    @abstractmethod
    def __get_type__(self):
        pass

    @abstractmethod
    def __get_personalityTrait__(self):
        pass

    @abstractmethod
    def __get_ideal__(self):
        pass

    @abstractmethod
    def __get_bond__(self):
        pass

    @abstractmethod
    def __set_equips__(self, personagem):
        pass

    @abstractmethod
    def __get_flaw__(self):
        pass
