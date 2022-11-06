from app.resources.racas.anao import Anao


class AnaoColina(Anao):
    def __init__(self, personagem):
        super().__init__()
        self.name = "ANÃO DA COLINA"
        self.__sub_description__ = "Como um anão da colina, você tem sentidos aguçados, maior intuição e notável " \
                                   "resiliência. Os anões dourados de Faerûn, que vivem em seu poderoso reino ao sul " \
                                   "do continente, são anões da colina, assim como os exilados Neidar e os " \
                                   "depreciáveis Klar de Krynn, no cenário de Dragonlance. "
        self.__add_skill__("Aumento no Valor de Habilidade", "Seu valor de Sabedoria aumenta em 1.")
        self.__add_skill__("Tenacidade Anã", " Seu máximo de pontos de vida aumentam em 1, e cada vez que o anão da "
                                             "colina sobe um nível, ele recebe 1 ponto de vida adicional.")
        self.__set_wisdom__(self.stats["wisdom"] + 1)
