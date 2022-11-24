from app.builders.prototipo.Equipamento import Equipamento


class Arma(Equipamento):
    def __init__(self, nome:str, preco: int, moeda: str, peso: float, quantidade: int, dano: str, propriedades: list):
        super().__init__(nome, preco, moeda, peso, quantidade)
        self.dano = dano
        self.propriedades = propriedades

    def __get_dano__(self):
        return self.dano

    def __set_dano__(self, dano):
        self.dano = dano

    def __get_propriedades__(self):
        return self.propriedades

    def __set_propriedades__(self, propriedades):
        self.propriedades = propriedades
