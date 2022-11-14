from app.builders.prototipo.Equipamento import Equipamento

class Armadura(Equipamento):
    def __init__(self, nome:str, preco: int, moeda: str, peso: float, quantidade: int, ca: int, furtividade: str):
        super().__init__(nome, preco, moeda, peso, quantidade)
        self.ca = ca
        self.furtividade = furtividade

    def __get_ca__(self):
        return self.ca

    def __set_ca__(self, ca):
        self.ca = ca

    def __get_furtividade__(self):
        return self.furtividade

    def __set_furtividade__(self, furtividade):
        self.furtividade = furtividade