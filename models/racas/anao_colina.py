from models.racas.anao import Anao

class AnaoColina(Anao):
    def __init__(self):
        super().__init__()
        self.add_habilidade("Aumento no Valor de Habilidade. Seu valor de Sabedoria aumenta em 1.")
        self.add_habilidade("Tenacidade Anã. Seu máximo de pontos de vida aumentam em 1, e cada vez que o anão da colina sobe um nível, ele recebe 1 ponto de vida adicional.")
        self.add_atributo(4, 1) # Adiciona 1 à sabedoria do Anão da Colina