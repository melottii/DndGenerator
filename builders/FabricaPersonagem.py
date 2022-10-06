from abc import ABC

from app.classes import barbaro, bruxo, ladino


class PersonaInterface(ABC):
    def __init__(self, chosen_class):
        self.name = str
        self.race = str
        self.person_class = str(chosen_class)
        self.trend = str
        self.body = list
        self.equip = list
        self.magic_tricks = list
        self.magic_spells = list
        self.tricks = list
        self.antecedent_type = str
        self.personality_trait = str
        self.ideal = str
        self.bond = str
        self.flaw = str
        self.dices = list
        self.expertise = list
        self.language = int
        self.idiom = list

    @staticmethod
    def build_class(person_class):
        try:
            match person_class.upper():
                case "BARBARO":
                    return barbaro.Barbaro()
                case "LADINO":
                    return ladino.Ladino()
                case "BRUXO":
                    return bruxo.Bruxo()
        except Exception as e:
            print(e)
            return e
