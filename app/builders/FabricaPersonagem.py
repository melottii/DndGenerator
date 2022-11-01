from abc import ABC

import random
import re
import sys
from unidecode import unidecode

from app.resources.classes import bruxo, barbaro, ladino
from app.resources.racas import halfling_pes_leves, halfling_robusto, anao_colina, anao_montanha
from app.resources.antecedentes import acolito, artesaoDeGuilda, charlatao


class PersonaInterface(ABC):
    def __init__(self):
        self.name = str
        self.life = 0
        self.armor_class = int
        self.body = []
        self.equip = []
        self.expertise = []
        self.knowledge = []
        self.idiom = {"rand": 0, "choice": []}
        self.trend = str
        self.race = None
        self.person_class = None
        self.background = None
        self.money = {"cobre (pc)": 0,
                      "prata (pp)": 0,
                      "electro (pe)": 0,
                      "ouro (po)": 0,
                      "platina (pl)": 0}
        self.dices = {"proficiency_bonus": str,
                      "resistence_test": [],
                      "rolls": {'strength': 0, 'dexterity': 0,
                                'constitution': 0, 'intelligence': 0,
                                'wisdom': 0, 'charisma': 0},
                      "modifiers": {'strength': 0, 'dexterity': 0,
                                    'constitution': 0, 'intelligence': 0,
                                    'wisdom': 0, 'charisma': 0}}
        self.magic = {"0": {str: []},
                      "1": {str: []}}

    def __set_name__(self, name: str):
        self.name = name

    def __set_race__(self, race: str):
        try:
            choices = ["ANAO DA COLINA", "ANAO DA MONTANHA", "HALFLING PÉS LEVES", "HALFLING ROBUSTO"]
            if race.upper() == "":
                race_name = random.choice(choices)
            else:
                race_name = re.sub("[0-9]", "", unidecode(race.upper()))
                if race_name not in choices:
                    race_name = random.choice(choices)
                else:
                    sys.exit("INPUT INCORRETO DE CLASSE")

            match race_name:
                case "ANAO DA COLINA":
                    self.race = anao_colina.AnaoColina(self)
                case "ANAO DA MONTANHA":
                    self.race = anao_montanha.AnaoMontanha(self)
                case "HALFLING PÉS LEVES":
                    self.race = halfling_pes_leves.HalflingPesLeves(self)
                case "HALFLING ROBUSTO":
                    self.race = halfling_robusto.HalflingRobusto(self)

        except Exception as e:
            sys.exit(f"ERRO AO DEFINIR RAÇA DO PERSONAGEM: {e}")

    def __set_class__(self, person_class: str):
        try:
            choices = ["BARBARO", "LADINO", "BRUXO"]
            if person_class.upper() == "":
                person_class_name = random.choice(choices)
            else:
                person_class_name = re.sub("[0-9]", "", unidecode(person_class.upper()))
                if person_class_name not in choices:
                    person_class_name = random.choice(choices)
                else:
                    sys.exit("INPUT INCORRETO DE CLASSE")
            person_class_name = "BARBARO"
            match person_class_name.upper():
                case "BARBARO":
                    self.person_class = barbaro.Barbaro(self)
                case "LADINO":
                    self.person_class = ladino.Ladino()
                case "BRUXO":
                    self.person_class = bruxo.Bruxo()
        except Exception as e:
            sys.exit(f"ERRO AO DEFINIR CLASSE DO PERSONAGEM: {e}")

    def __set_status__(self):
        for attribute in self.dices["rolls"].keys():
            total, dice = 0, []
            for x in range(4):
                dice.append(random.randint(1, 6))
            dice.remove(min(dice))
            for m in dice:
                total += m
            self.dices["rolls"][attribute] += total
            self.dices["modifiers"][attribute] = -5 + (self.dices["rolls"][attribute] // 2)

    def __set_trend__(self):
        opt = ["Leal e Bom", "Leal e Neutro", "Leal e Mau",
               "Neutro e Bom", "Neutro e Mau", "Neutro",
               "Caótico e Bom", "Caótico e Neutro", "Caótico e Mau"]
        self.trend = random.choice(opt)

    def __set_background__(self, background: str):
        choices = ["ARTESAO DE GUILDA", "ACOLITO", "CHARLATAO"]
        if background.upper() == "":
            background_name = random.choice(choices)
        else:
            background_name = re.sub("[0-9]", "", unidecode(background.upper()))
            if background_name not in choices:
                background_name = random.choice(choices)
        match background_name:
            case "ARTESAO DE GUILDA":
                self.background = artesaoDeGuilda.ArtesaoDeGuilda(self)
            case "ACOLITO":
                self.background = acolito.Acolito(self)
            case "CHARLATAO":
                self.background = charlatao.Charlatao(self)

    def director(self, name: str, race: str, chosen_class: str, background: str):
        PersonaInterface.__set_name__(self, name)
        PersonaInterface.__set_trend__(self)
        PersonaInterface.__set_race__(self, race)
        PersonaInterface.__set_status__(self)
        PersonaInterface.__set_background__(self, background)
        PersonaInterface.__set_class__(self, chosen_class)
