from app.builders.fabrica_abstrata.Classe import Classe
import random


class Ladino(Classe):
    def __init__(self, personagem):
        super().__init__()
        self.name = "LADINO"
        self.proficiency_bonus = "+2"
        self.life = 8 + int(personagem.dices["modifiers"]["constitution"])
        self.dices_life = "1d8"
        self.knowledge =  ["Armaduras leves", "Armas simples", "Bestas de mão",
                                    "Espadas longas", "Rapieiras", "Espadas curtas", "Ferramentas de ladrão"]
        self.expertise = Ladino.__set_skill_list__(personagem)
        self.equip = Ladino.__set_equip_list__(personagem)
        self.endurance_tests = ["dexterity", "intelligence"]
        Ladino.__set_config__(self, personagem)

    @staticmethod
    def __set_skill_list__(personagem):
        rogue_list = ["Acrobacia", "Atletismo", "Atuação", "Enganação", 
                                "Furtividade", "Intimidação", "Intuição", "Investigação",
                                "Percepção", "Persuasão", "Prestidigitação"]
        final_list = [i for i in rogue_list if i not in personagem.expertise]
        return random.choices(final_list, k=2)

    @staticmethod
    def __set_equip_list__(personagem):
        try:
            equips = {"Armas": {}, "Armaduras": {}, "Equipamentos": []}
            a = random.choice(["Rapieira", "Espada Longa"])
            if a == "Rapieira":
                equips["Armas"]["Rapieira"] = personagem.bag["Armas"].__get_corpo_a_corpo_marcial__(
                    "Rapieira")
            else:
                equips["Armas"]["Espada Longa"] = personagem.bag["Armas"].__get_corpo_a_corpo_marcial__("Espada Longa")
            b = random.choice(["Machadinha", "Arma simples"])
            if b == "Machadinha":
                equips["Armas"]["Machadinha 1"] = personagem.bag["Armas"].__get_corpo_a_corpo_simples__("Machadinha")
                equips["Armas"]["Machadinha 2"] = personagem.bag["Armas"].__get_corpo_a_corpo_simples__("Machadinha")
            else:
                a_random = random.choice(personagem.bag["Armas"].__get_corpo_a_corpo_simples_list__())
                equips["Armas"][a_random] = personagem.bag["Armas"].__get_corpo_a_corpo_simples__(a_random)
            for i in range(1, 5):
                equips["Armas"]["Azagaia " + str(i)] = personagem.bag["Armas"].__get_corpo_a_corpo_simples__("Azagaia")
            equips["Equipamentos"].append(
                {"Pacote de Aventureiro": personagem.bag["Equipamentos"].__get_pacote__("Pacote de Aventureiro")})
            return equips
        except Exception as e:
            print(e)

    def get_name(self):
        return f"CLASSE: {self.name}"

    def __set_config__(self, personagem):
        personagem.life += self.life
        for i in self.endurance_tests:
            personagem.dices["resistence_test"].append(i)
        personagem.proficiency_bonus = self.proficiency_bonus

        for n in self.knowledge:
            personagem.knowledge.append(n)

        for m in self.expertise:
            personagem.expertise.append(m)

        for e in self.equip:
            if e != "Equipamentos":
                for k in self.equip[e]:
                    personagem.equip[e][k] = self.equip[e][k]
            else:
                for b in range(len(self.equip[e])):
                    personagem.equip[e].append(self.equip[e][0])
