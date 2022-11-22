from app.builders.fabrica_abstrata.Classe import Classe
from app.builders.prototipo.ItemPrototipo import ItemPrototipo

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
        self.equip = Barbaro.__set_equip__(personagem)
        self.endurance_tests = ["strength", "constitution"]

    @staticmethod
    def __set_skill_list__(personagem):
        barbarian_list = ["Adestrar Animais", "Atletismo", "Intimidação", "Natureza", "Percepção", "Sobrevivência"]
        final_list = [i for i in barbarian_list if i not in personagem.expertise]
        return random.choices(final_list, k=2)

    @staticmethod
    def __set_equip__(personagem):
        try:
            prototipo = ItemPrototipo()

            a = random.choice(["Machado Grande", "Arma Marcial"])
            item = None
            item2 = None

            if a == "Machado Grande":
                item = prototipo.get_arma_marcial(a)
            else:
                item = prototipo.get_random_arma_marcial()
            personagem.equip["Armas"].append(item)

            b = random.choice(["Machadinha", "Arma simples"])
            if b == "Machadinha":
                item = prototipo.get_arma_corpo_a_corpo_simples(b)
                item2 = prototipo.get_arma_corpo_a_corpo_simples(b)
            else:
                item = prototipo.get_random_arma_corpo_a_corpo_simples()

            personagem.equip["Armas"].append(item)
            if item2 is not None:
                personagem.equip["Armas"].append(item2)

            for i in range(1, 5):
                item = prototipo.get_arma_corpo_a_corpo_simples("Azagaia")
                personagem.equip["Armas"].append(item)

            pacote = prototipo.get_pacote("Pacote de Aventureiro")
            prototipo.add_equipamentos_pacote(pacote, personagem)
            print(prototipo)

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
