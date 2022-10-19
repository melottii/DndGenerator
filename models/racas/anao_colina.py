from models.racas.anao import Anao

class AnaoColina(Anao):
    def __init__(self):
        super().__init__()
        self.__add_skill__("Aumento no Valor de skill. Seu valor de Sabedoria aumenta em 1.")
        self.__add_skill__("Tenacidade Anã. Seu máximo de pontos de vida aumentam em 1, e cada vez que o anão da colina sobe um nível, ele recebe 1 ponto de vida adicional.")
        self.__set_sabedoria__(self.sabedoria+1)