from abc import ABC

import random
import re
import sys
from unidecode import unidecode

from app.resources.classes import bruxo, barbaro, ladino
from app.resources.racas import draconato, humano, anao
from app.resources.antecedentes import acolito, artesaoDeGuilda, charlatao


class PersonaInterface(ABC):
    def __init__(self):
        self.name = str
        self.body = []
        self.equip = []
        self.expertise = []
        self.knowledge = []
        self.idiom = {"rand": 0, "choice": []}
        self.trend = str
        self.race = str
        self.person_class = str
        self.money = {"cobre (pc)": 0,
                      "prata (pp)": 0,
                      "electro (pe)": 0,
                      "ouro (po)": 0,
                      "platina (pl)": 0}
        self.dices = {
            "rolls": {'strength': 0, 'dexterity': 0,
                      'constitution': 0, 'intelligence': 0,
                      'wisdom': 0, 'charisma': 0},
            "modifiers": {'strength': 0, 'dexterity': 0,
                          'constitution': 0, 'intelligence': 0,
                          'wisdom': 0, 'charisma': 0}}
        self.magic = {"spells": {"0": {str: []},
                                 "1": {str: []}}}
        self.background_format = {"name": str,
                                  "type": str,
                                  "personality_trait": [str, str],
                                  "ideal": str,
                                  "bond": str,
                                  "flaw": str}

    def __set_name__(self, name):
        self.name = name

    def __set_race__(self, race):
        try:
            race = re.sub('[0-9]', '', unidecode(race.upper()))
            match race:
                case "ANAO":
                    self.race = anao.Anao()
                case "DRACONATO":
                    self.race = draconato.Draconato()
                case "HUMANO":
                    self.race = humano.Humano()
        except Exception as e:
            sys.exit(f"ERRO AO DEFINIR RAÇA DO PERSONAGEM: {e}")

    def __set_class__(self, person_class):
        try:
            person_class = re.sub('[^A-Z]', '', unidecode(person_class.upper()))
            match person_class.upper():
                case "BARBARO":
                    self.person_class = barbaro.Barbaro()
                case "LADINO":
                    self.person_class = ladino.Ladino()
                case "BRUXO":
                    self.person_class = bruxo.Bruxo()
        except Exception as e:
            sys.exit(f"ERRO AO DEFINIR CLASSE DO PERSONAGEM: {e}")

    def __set_status__(self):
        for i in self.dices["rolls"]:
            total, dice = 0, []
            for x in range(4):
                dice.append(random.randint(1, 6))
            dice.remove(min(dice))
            for m in dice:
                total += m
            self.dices["rolls"][i] = total

    def __set_trend__(self):
        opt = ["Leal e Bom", "Leal e Neutro", "Leal e Mau"
               "Neutro e Bom", "Neutro e Mau", "Neutro"
               "Caótico e Bom", "Caótico e Neutro", "Caótico e Mau"]
        self.trend = random.choice(opt)

    def __set_background__(self, background):
        choices = ["ARTESAO DE GUILDA", "ACOLITO", "CHARLATAO"]
        if background.upper() is None:
            background_name = random.choice(choices)
        else:
            background_name = re.sub("[0-9]", "", unidecode(background.upper()))
            if background_name not in choices:
                background_name = random.choice(choices)
        match background_name:
            case "ARTESAO DE GUILDA":
                artesaoDeGuilda.ArtesaoDeGuilda(self)
            case "ACOLITO":
                acolito.Acolito(self)
            case "CHARLATAO":
                charlatao.Charlatao(self)

    def director(self, name: str, race: str, chosen_class: str, background: str):
        PersonaInterface.__set_name__(self, name)
        PersonaInterface.__set_trend__(self)
        PersonaInterface.__set_race__(self, race)
        PersonaInterface.__set_class__(self, chosen_class)
        PersonaInterface.__set_status__(self)
        PersonaInterface.__set_background__(self, background)
