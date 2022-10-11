from builders.Classe import Classe
import random


class Anao(Classe):
    def __init__(self):
        super().__init__()
        self.name = "ANÃO"
        self.race_variancy = Anao.get_race_variancy()

    def get_name(self):
        return "RAÇA: " + self.name

    def get_race_variancy(self):
        return "VARIAÇÃO DA RAÇA: " + random.choice(["Hill Dwarf", "Montain Dwarf"])

    def get_modifier(self):
        return {"constitution": 2, "strength": 2}
