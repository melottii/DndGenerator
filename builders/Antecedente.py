from abc import ABC, abstractmethod


class Antecedente(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_personality_trait(self):
        pass

    @abstractmethod
    def get_ideal(self):
        pass

    @abstractmethod
    def get_bond(self):
        pass

    @abstractmethod
    def get_flaw(self):
        pass
