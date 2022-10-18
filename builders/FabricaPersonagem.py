from abc import ABC

import random
import re
import unidecode

from app.classes import barbaro, bruxo, ladino
from app.racas import anao, draconato, humano
from app.antecedentes import artesaoDeGuilda


class PersonaInterface(ABC):
    def __init__(self, name: str, race: str, chosen_class: str, background: str):
        self.name = name
        self.body = []
        self.equip = []
        self.money = {"cobre (pc)": 0,
                      "prata (pp)": 0,
                      "electro (pe)": 0,
                      "ouro (po)": 0,
                      "platina (pl)": 0
        }
        self.expertise = []
        self.language = 0
        self.idiom = []
        self.trend = PersonaInterface.trend_definition()

        self.roll_dices = {
            "rolls": {'strength': 0, 'dexterity': 0,
                      'constitution': 0, 'intelligence': 0,
                      'wisdom': 0, 'charisma': 0},
            "modifiers": {'strength': 0, 'dexterity': 0,
                          'constitution': 0, 'intelligence': 0,
                          'wisdom': 0, 'charisma': 0}
        }
        self.dices = PersonaInterface.status(self.roll_dices)
        self.race = PersonaInterface.build_race(race)
        self.person_class = PersonaInterface.build_class(chosen_class)
        self.magic = {"tricks": list,
                      "spells": {"0": None,
                                 "1": None}}

        self.background_format = {"name": None,
                                  "type": None,
                                  "personality_trait": None,
                                  "ideal": None,
                                  "bond": None,
                                  "flaw": None}

        self.antecedent = PersonaInterface.background_settings(self, background)

    @staticmethod
    def build_race(race):
        try:
            race = re.sub('[^A-Z]', '', unidecode.unidecode(race.upper()))
            print(race)
            match race:
                case "ANAO":
                    return anao.Anao()
                case "DRACONATO":
                    return draconato.Draconato()
                case "HUMANO":
                    return humano.Humano()
        except Exception as e:
            print(e)
            return e

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

    @staticmethod
    def status(roll_dices):
        for i in roll_dices["rolls"]:
            total, dice = 0, []
            for x in range(4):
                dice.append(random.randint(1, 6))
            dice.remove(min(dice))
            for m in dice:
                total += m
            roll_dices["rolls"][i] = total
        return roll_dices

    @staticmethod
    def trend_definition():
        opt = ["Leal e Bom", "Leal e Neutro", "Leal e Mau"
               "Neutro e Bom", "Neutro e Mau", "Neutro"
               "Caótico e Bom", "Caótico e Neutro", "Caótico e Mau"]
        trend = random.choice(opt)
        return trend

    @staticmethod
    def background_settings(self, background):
        choices = ["ARTESAODEGUILDA", "ACOLITO", "CHARLATAO"]
        if background.upper() is None:
            background_name = random.choice(choices)
        else:
            background_name = re.sub("[^A-Z]", "", unidecode.unidecode(background.upper()))
            if background_name not in choices:
                background_name = random.choice(choices)
        match background_name:
            case "ARTESAODEGUILDA":
                return artesaoDeGuilda.ArtesaoDeGuilda(self)
            case "ACOLITO":
                pass
            case "CHARLATAO":
                pass
