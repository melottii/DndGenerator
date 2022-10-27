from app.builders.Classe import Classe
import random


class Barbaro(Classe):
    def __init__(self, personagem):
        super().__init__()
        self.name = "BÁRBARO"
        self.endurance_tests = ["Força", "Constituição  "]
        self.life = 12 + int(personagem.dices["modifiers"]["constitution"])
        self.dices_life = "1d12"
        self.knowledge = ["Armaduras leves", "Armaduras médias", "Escudos", "Armas simples", "Armas simples"]
        self.expertise = Barbaro.__set_skill_list__(personagem)

        Barbaro.__set_config__(self, personagem)

    @staticmethod
    def __set_skill_list__(personagem):
        barbarian_list = ["Adestrar Animais", "Atletismo", "Intimidação", "Natureza", "Percepção", "Sobrevivência"]
        final_list = [i for i in barbarian_list if i not in personagem.expertise]
        return random.choices(final_list, k=2)

    def get_name(self):
        return f"CLASSE: {self.name}"

    def __set_config__(self, personagem):
        personagem.life += self.life
        pass
