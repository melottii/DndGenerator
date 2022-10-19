from app.builders.Classe import Classe
import random


class Anao(Classe):
    def __init__(self):
        super().__init__()
        self.name = "ANÃO"
        self.race_variancy = random.choice(["Hill Dwarf", "Montain Dwarf"])

    def get_name(self):
        return "RAÇA: " + self.name

    def get_race_variancy(self):
        return "VARIAÇÃO DA RAÇA: " + self.race_variancy

    def get_modifier(self):
        try:
            match self.race_variancy:
                case "HILL DWARF":
                    return {"constitution": 2, "strength": 2}
                case "MONTAIN DWARF":
                    return {"constitution": 2, "strength": 2}

        except Exception as e:
            print(e)
            return