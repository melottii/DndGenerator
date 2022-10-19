from app.resources.racas.anao import Anao


class AnaoMontanha(Anao):
    def __init__(self):
        super().__init__()
        self.__sub_description__ = "Como um anão da montanha, você é forte e resistente, acostumados a uma vida " \
                                   "difícil em terrenos difíceis. Você, provavelmente tem a descendência daqueles " \
                                   "mais altos (para um anão) e tende a possuir uma coloração mais clara. Os anões " \
                                   "do escudo do norte de Faerûn, bem como o clã governante Hylar e os clãs nobres " \
                                   "Daewar de Dragonlance, são anões da montanha. "
        self.__add_skill__("Aumento no Valor de Habilidade. Seu valor de Força aumenta em 2.")
        self.__add_skill__("Treinamento Anão com Armaduras. Você adquire proficiência em armaduras leves e médias. ")
        self.__set_strength__(self.stats["strength"] + 2)

    def __get_sub_description__(self):
        return self.__sub_description__

    def __set_sub_description__(self, sub_description):
        self.__sub_description__ = sub_description

    def __set_description__(self, description):
        pass

    def __get_stats__(self):
        pass

    def __set_stats__(self, stats):
        pass

    def __add_atributo__(self, atributo, quantidade):
        pass
