class Equipamento:
    def __init__(self, nome:str, preco: int, moeda: str, peso: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.moeda = moeda
        self.peso = peso
        self.quantidade = quantidade

    def __get_nome__(self):
        return self.nome

    def __set_nome__(self, nome):
        self.nome = nome

    def __get_preco__(self):
        return self.preco

    def __set_preco__(self, preco):
        self.preco = preco

    def __get_moeda__(self):
        return self.moeda

    def __set_moeda__(self, moeda):
        self.moeda = moeda

    def __get_peso__(self):
        return self.peso

    def __set_peso__(self, peso):
        self.peso = peso

    def __get_quantidade__(self):
        return self.quantidade

    def __set_quantidade__(self, quantidade):
        self.quantidade = quantidade
