from interface.fabricaPersonagem import personaInterface

class instanciaLadino(personaInterface):

    def __init__(self, nome) -> dict:
        self.raca = {
            'nome': 'Ladino'
            'proeficiencias': None,
        
        }
        return self.raca