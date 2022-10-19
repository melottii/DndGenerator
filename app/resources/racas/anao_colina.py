from app.resources.racas.anao import Anao


class AnaoColina(Anao):
    def __init__(self):
        super().__init__()
        self.__sub_description__ = "Como um anão da colina, você tem sentidos aguçados, maior intuição e notável "\
                                   "resiliência. Os anões dourados de Faerûn, que vivem em seu poderoso reino ao sul "\
                                   "do continente, são anões da colina, assim como os exilados Neidar e os "\
                                   "depreciáveis Klar de Krynn, no cenário de Dragonlance. "
        self.__add_skill__("Aumento no Valor de skill. Seu valor de Sabedoria aumenta em 1.")
        self.__add_skill__("Tenacidade Anã. Seu máximo de pontos de vida aumentam em 1, e cada vez que o anão da "
                           "colina sobe um nível, ele recebe 1 ponto de vida adicional.")
        self.__set_wisdom__(self.stats["wisdom"] + 1)

    def __set_sabedoria__(self, param):
        pass

    def __set_description__(self, description):
        pass

    def __get_stats__(self):
        pass

    def __set_stats__(self, stats):
        pass

    def __add_atributo__(self, atributo, quantidade):
        pass
