from abc import ABC, abstractmethod


class Classe(ABC):
    @abstractmethod
    def __get_name__(self):
        pass

    def __get_proficiency_bonus__(self):
        pass

    def __get_life__(self):
        pass

    def __get_dices_life__(self):
        pass

    def __get_knowledge__(self):
        pass

    def __get_expertise__(self):
        pass

    def __get_equip__(self):
        pass

    def __get_endurance_tests__(self):
        pass

    def __get_skills__(self):
        pass

    def __set_name__(self, vlr):
        pass

    def __set_proficiency_bonus__(self, vlr):
        pass

    def __set_life__(self, vlr):
        pass

    def __set_dices_life__(self, vlr):
        pass

    def __set_knowledge__(self, vlr):
        pass

    def __set_expertise__(self, vlr):
        pass

    def __set_endurance_tests__(self, vlr):
        pass

    def __set_skills__(self, chave, vlr):
        pass
