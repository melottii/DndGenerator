from abc import ABC, abstractmethod


class Raca(ABC):

    @abstractmethod
    def __get_name__(self):
        pass
    
    @abstractmethod
    def __set_name__(self, name):
        pass

    @abstractmethod
    def __get_description__(self):
        pass
    
    @abstractmethod
    def __set_description__(self, description):
        pass

    @abstractmethod
    def __get_restrictions__(self):
        pass
    
    @abstractmethod
    def __set_restrictions__(self, restrictions):
        pass
    
    @abstractmethod
    def __get_skills__(self):
        pass
    
    @abstractmethod
    def __set_skills__(self, skills):
        pass

    @abstractmethod
    def __add_skill__(self, skill):
        pass

    @abstractmethod
    def __get_magic__(self):
        pass
    
    @abstractmethod
    def __set_magic__(self, magic):
        pass

    @abstractmethod
    def __get_strength__(self):
        pass
    
    @abstractmethod
    def __set_strength__(self, strength):
        pass

    @abstractmethod
    def __get_dexterity__(self):
        pass
    
    @abstractmethod
    def __set_dexterity__(self, dexterity):
        pass
    
    @abstractmethod
    def __get_constitution__(self):
        pass
    
    @abstractmethod
    def __set_constitution__(self, constitution):
        pass
    
    @abstractmethod
    def __get_wisdom__(self):
        pass
    
    @abstractmethod
    def __set_wisdom__(self, wisdom):
        pass
    
    @abstractmethod
    def __get_intelligence__(self):
        pass
    
    @abstractmethod
    def __set_intelligence__(self, intelligence):
        pass

    @abstractmethod
    def __get_charisma__(self):
        pass
    
    @abstractmethod
    def __set_charisma__(self, charisma):
        pass

    @abstractmethod
    def __set_config__(self, personagem):
        pass
