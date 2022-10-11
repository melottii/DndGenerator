from abc import ABC

import random

from app.classes import barbaro, bruxo, ladino
from app.racas import anao, draconato, elfo, gnomo, halfling, humano, meioElfo, meioOrc, tiefling


class PersonaInterface(ABC):
    def __init__(self, name: str, race: str, chosen_class: str, dices: list):

        roll_dices = {
            "rolls": {
                'strength': dices[0], 'dexterity': dices[1],
                'constitution': dices[2], 'intelligence': dices[3],
                'wisdom': dices[4], 'charisma': dices[5]
            },
            "modifiers": {
                'strength': 0, 'dexterity': 0,
                'constitution': 0, 'intelligence': 0,
                'wisdom': 0, 'charisma': 0
            }
        }

        self.dices = PersonaInterface.status(roll_dices)
        self.name = str(name)
        self.race = PersonaInterface.build_race(race)
        self.person_class = PersonaInterface.build_class(chosen_class)
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
        self.expertise = list
        self.language = int
        self.idiom = list

    @staticmethod
    def build_race(race, roll_dices):
        try:
            match race.upper():
                case "ANAO":
                    return anao.Anao()
                case "DRACONATO":
                    return draconato.Draconato()
                case "ELFO":
                    return elfo.Elfo()
                case "GNOMO":
                    return gnomo.Gnomo()
                case "HALFLING":
                    return halfling.Halfling()
                case "HUMANO":
                    return humano.Humano()
                case "MEIO-ELFO":
                    return meioElfo.MeioElfo()
                case "MEIO-ORC":
                    return meioOrc.MeioOrc()
                case "TIEFLING":
                    return tiefling.Tiefling()
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
            if roll_dices["rolls"][i] == 0:
                total, dice = 0, []
                for x in range(4):
                    dice.append(random.randint(1, 6))
                dice.remove(min(dice))
                for m in dice:
                    total += m
                roll_dices["rolls"][i] = total
            else:
                total = roll_dices["rolls"][i]
            roll_dices["modifiers"][i] = (total//2) - 5
        return roll_dices
