from abc import ABC, abstractmethod

class Raca(ABC):

    @abstractmethod
    def get_nome(self):
        pass
    
    @abstractmethod
    def set_nome(self, nome):
        pass

    @abstractmethod
    def get_descricao(self):
        pass
    
    @abstractmethod
    def set_desricao(self, descricao):
        pass

    @abstractmethod
    def get_restricoes(self):
        pass
    
    @abstractmethod
    def set_restricoes(self, restricoes):
        pass
    
    @abstractmethod
    def get_habilidadesUnicas(self):
        pass
    
    @abstractmethod
    def set_habilidadesUnicas(self, habilidadesUnicas):
        pass

    @abstractmethod
    def add_habilidade(self, habilidade):
        pass

    @abstractmethod
    def get_magias(self):
        pass
    
    @abstractmethod
    def set_magias(self, magias):
        pass

    @abstractmethod
    def get_forca(self):
        pass
    
    @abstractmethod
    def set_forca(self, forca):
        pass

    @abstractmethod
    def get_destreza(self):
        pass
    
    @abstractmethod
    def set_destreza(self, destreza):
        pass
    
    @abstractmethod
    def get_constituicao(self):
        pass
    
    @abstractmethod
    def set_constituicao(self, constituicao):
        pass
    
    @abstractmethod
    def get_sabedoria(self):
        pass
    
    @abstractmethod
    def set_sabedoria(self, sabedoria):
        pass
    
    @abstractmethod
    def get_inteligencia(self):
        pass
    
    @abstractmethod
    def set_inteligencia(self, inteligencia):
        pass

    @abstractmethod
    def get_carisma(self):
        pass
    
    @abstractmethod
    def set_carisma(self, carisma):
        pass
    
    @abstractmethod
    def add_atributo(self, atributo, quantidade):
        pass
