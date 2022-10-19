from abc import ABC, abstractmethod


class Antecedente(ABC):
    @abstractmethod
    def get_name(self, personagem):
        pass

    @abstractmethod
    def get_type(self, personagem):
        pass

    @abstractmethod
    def get_personality_trait(self, personagem):
        pass

    @abstractmethod
    def get_ideal(self, personagem):
        pass

    @abstractmethod
    def get_bond(self, personagem):
        pass

    @abstractmethod
    def get_flaw(self, personagem):
        pass
