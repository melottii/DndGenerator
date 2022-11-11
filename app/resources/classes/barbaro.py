from app.builders.Classe import Classe
import random


class Barbaro(Classe):
    def __init__(self, personagem):
        super().__init__()
        self.name = "BÁRBARO"
        self.proficiency_bonus = "+2"
        self.life = 12 + int(personagem.dices["modifiers"]["constitution"])
        self.dices_life = "1d12"
        self.knowledge = ["Armaduras leves", "Armaduras médias", "Escudos", "Armas simples", "Armas simples"]
        self.expertise = Barbaro.__set_skill_list__(personagem)
        self.equip = Barbaro.__set_equip_list__(personagem)
        self.endurance_tests = ["strength", "constitution"]
        Barbaro.__set_config__(self, personagem)

    @staticmethod
    def __set_skill_list__(personagem):
        barbarian_list = ["Adestrar Animais", "Atletismo", "Intimidação", "Natureza", "Percepção", "Sobrevivência"]
        final_list = [i for i in barbarian_list if i not in personagem.expertise]
        return random.choices(final_list, k=2)

    @staticmethod
    def __set_equip_list__(personagem):
        try:
            equips = {"Armas": {}, "Armaduras": {}, "Equipamentos": []}
            a = random.choice(["Machado Grande", "Arma Marcial"])
            if a == "Machado Grande":
                equips["Armas"]["Machado Grande"] = personagem.bag["Armas"].__get_corpo_a_corpo_marcial__(
                    "Machado Grande")
            else:
                a_random = random.choice(personagem.bag["Armas"].__get_corpo_a_corpo_marcial_list__())
                equips["Armas"][a_random] = personagem.bag["Armas"].__get_corpo_a_corpo_marcial__(a_random)
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
