class Pacote:
    def __init__(self, nome: str, preco: int, moeda: str, itens):
        self.nome = nome
        self.preco = preco
        self.moeda = moeda
        self.itens = itens
    
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

    def __set_moeda__(self, nome):
        self.nome = nome
    
    def __get_itens__(self):
        return self.itens

    def __set_itens__(self, itens):
        self.itens = itens
    
    def __set_config__(self, personagem):
        for item in self.itens:
            personagem.equip["Equipamentos"].append(item)
