from datetime import datetime
import json
import os
import re

from app.builders.BuilderPersonagem import BuilderPersonagem
from interface.sessao import *

class DndGenerator:
    def __init__(self):
        self.user = login("vinicius@gmail.com", "123")
        self.character = BuilderPersonagem()

    def define_escolhas(self):
        chosen_name = input("Nome do personagem: ")
        print("\nRaças cadastradas:")
        rc = {"1": "Anão da Colina",
              "2": "Anao da Montanha",
              "3": "Halfling Pés Leves",
              "4": "Halfling Robusto"}
        for a in rc:
            print(f"{a} - {rc[a]}")
        chosen_race = input("Número da Raça escolhida: ")
        if chosen_race not in rc:
            chosen_race = ""
        else:
            chosen_race = rc[chosen_race]

        cl = {"1": "Bárbaro",
              "2": "Bruxo",
              "3": "Ladino"}
        print("\nClasses Cadastradas:")
        for a in cl:
            print(f"{a} - {cl[a]}")
        chosen_class = input("Número da Classe escolhida: ")
        if chosen_class not in cl:
            chosen_class = ""
        else:
            chosen_class = cl[chosen_class]

        ant = {"1": "Acólito",
               "2": "Artesão de Guilda",
               "3": "Charlatão"}
        print("\nAntecedentes Cadastrados:")
        for a in ant:
            print(f"{a} - {ant[a]}")
        chosen_background = input("Número do Antecedente escolhido: ")
        if chosen_background not in ant:
            chosen_background = ""
        else:
            chosen_background = ant[chosen_background]
        print()
        return chosen_name, chosen_race, chosen_class, chosen_background

    def printa_usuario(self):
        print(self.user.nome)
        print(self.user.email)

    def printa_personagem(self):
        print(self.define_equipamentos())
        """
        print(self.character.name)
        print(self.character.race.name)
        print(self.character.person_class.name)
        print(self.character.trend)
        print(self.character.money)
        self.printa_equipamentos()
        print(self.character.dices["rolls"])
        print(self.character.dices["modifiers"])
        print(self.character.background.background_format["name"])
        print(self.character.background.background_format["type"])
        print(self.character.background.background_format["personality_trait"][0])
        print(self.character.background.background_format["personality_trait"][1])
        print(self.character.background.background_format["ideal"])
        print(self.character.background.background_format["flaw"])
        print(self.character.background.background_format["bond"])
        print("Truques: ", list(self.character.magic[0].keys()))
        print("Magias: ", list(self.character.magic[1].keys()))
        """

    def define_equipamentos(self):
        equipamentos = {}
        for tipo in self.character.equip:
            equipamentos[tipo.upper()] = {}
            for equipamento in self.character.equip[tipo]:
                equipamentos[tipo.upper()][equipamento.nome] = {"PREÇO": equipamento.preco,
                                                                "MOEDA": equipamento.moeda,
                                                                "PESO": equipamento.peso,
                                                                "QUANTIDADE": equipamento.quantidade}
        return equipamentos

    def json_output(self):
        date_now = re.sub(r"[.\:\-\ ]", "", str(datetime.now()))
        person_name = re.sub(r"[.\:\-\ ]", "", str(self.character.name))+"_" \
            if re.sub(r"[.\:\-\ ]", "", str(self.character.name)) != "" else ""
        json_file = open(os.path.join(f"..\\DndGenerator\\app\\outputs\\{person_name + date_now}.json"), 'w')
        data = {person_name: {
            "NAME": self.character.name,
            "RACE": {"NAME": self.character.race.name,
                     "DESCRIPTION": self.character.race.__get_description__(),
                     "RESTRICTION": self.character.race.__get_restrictions__(),
                     "SKILLS": self.character.race.__get_skills__(),
                     },
            "CLASS": {"NAME": self.character.person_class.__get_name__(),
                      "DICES LIFE": self.character.person_class.__get_dices_life__(),
                      "SKILLS": self.character.person_class.__get_skills__()
                      },
            "TREND": self.character.trend,
            "LIFE": self.character.life,
            "ARMOR CLASS": self.character.armor_class,
            "DICES": self.character.dices,
            "EQUIP": DndGenerator.define_equipamentos(self),
            "EXPERTISE": self.character.expertise,
            "KNOWLEDGE": self.character.knowledge,
            "IDIOM": self.character.idiom,
            "BACKGROUND": {"NAME": self.character.background.__get_name__(),
                           "TYPE": self.character.background.__get_type__(),
                           "PERSONALITY TRAIT": self.character.background.__get_personalityTrait__(),
                           "IDEAL": self.character.background.__get_ideal__(),
                           "BOND": self.character.background.__get_bond__(),
                           "FLAW": self.character.background.__get_flaw__()
                           },
            "MONEY": self.character.money,
            "MAGIC": self.character.magic
        }}
        json.dump(data, json_file, indent=1)


if __name__ == "__main__":
    first_person = DndGenerator()
    chosen = first_person.define_escolhas()
    first_person.character = first_person.character.director(chosen[0], chosen[1], chosen[2], chosen[3])
    # first_person.printa_personagem()
    first_person.json_output()