from app.builders.fabrica_abstrata.Classe import Classe
from app.builders.prototipo.ItemPrototipo import ItemPrototipo

import random


class Ladino(Classe):
    def __init__(self, personagem):
        super().__init__()
        self.name = "LADINO"
        self.proficiency_bonus = "+2"
        self.life = 8 + int(personagem.dices["modifiers"]["constitution"])
        self.dices_life = "1d8"
        self.knowledge = ["Armaduras leves", "Armas simples", "Bestas de mão",
                          "Espadas longas", "Rapieiras", "Espadas curtas", "Ferramentas de ladrão"]
        self.expertise = Ladino.__set_skill_list__(personagem)
        self.equip = Ladino.__set_equip__(personagem)
        self.endurance_tests = ["dexterity", "intelligence"]

    @staticmethod
    def __set_skill_list__(personagem):
        rogue_list = ["Acrobacia", "Atletismo", "Atuação", "Enganação", 
                      "Furtividade", "Intimidação", "Intuição", "Investigação",
                      "Percepção", "Persuasão", "Prestidigitação"]
        final_list = [i for i in rogue_list if i not in personagem.expertise]
        return random.choices(final_list, k=2)

    @staticmethod
    def __set_equip__(personagem):
        try:
            prototipo = ItemPrototipo()

            a = random.choice(["Rapieira", "Espada Longa"])
            item2 = None
            item3 = None

            item = prototipo.get_arma_marcial(a)
            personagem.equip["Armas"].append(item)

            b = random.choice(["Arco Curto", "Espada Curta"])
            if b == "Arco Curto":
                item = prototipo.get_arma_distancia_simples(b)
                item2 = prototipo.get_equipamento("Aljava", 1)
                item3 = prototipo.get_equipamento("Flechas (20)", 1)
            else:
                item = prototipo.get_arma_marcial(b)

            personagem.equip["Armas"].append(item)
            if item2 is not None:
                personagem.equip["Equipamentos"].append(item2)
            if item3 is not None:
                personagem.equip["Equipamentos"].append(item3)

            item = prototipo.get_armadura_leve("Couro")
            personagem.equip["Armaduras"].append(item)

            item = prototipo.get_arma_corpo_a_corpo_simples("Adaga")
            personagem.equip["Armas"].append(item)
            item = prototipo.get_arma_corpo_a_corpo_simples("Adaga")
            personagem.equip["Armas"].append(item)

            item = prototipo.get_equipamento("Ferramentas de ladrão", 1)
            personagem.equip["Equipamentos"].append(item)

            nome = random.choice(["Pacote de Assaltante", "Pacote de Aventureiro", "Pacote de Explorador"])
            pacote = prototipo.get_pacote(nome)
            prototipo.add_equipamentos_pacote(pacote, personagem)

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
