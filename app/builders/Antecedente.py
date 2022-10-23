from abc import ABC, abstractmethod


class Antecedente(ABC):
    def __init__(self, name, equips, idiom, expertise, knowledge, money, background_format):
        self.name = name
        self.equips = equips
        self.idiom = idiom
        self.expertise = expertise
        self.knowledge = knowledge
        self.money = money
        self.background_format = background_format

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
