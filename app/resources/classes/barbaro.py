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
        self.skills = {"FÚRIA": "Em batalha, você luta com uma ferocidade primitiva. No seu turno, você pode entrar em "
                                "fúria com uma ação bônus. Enquanto estiver em fúria, você recebe os seguintes "
                                "benefícios se você não estiver vestindo uma armadura pesada:  Você tem vantagem em "
                                "testes de Força e testes de resistência de Força.  Quando você desferir um ataque "
                                "com arma corpo-acorpo usando Força, você recebe um bônus nas jogadas de dano que "
                                "aumenta à medida que você adquire níveis de bárbaro, como mostrado na coluna Dano de "
                                "Fúria na tabela O Bárbaro.  Você possui resistência contra dano de concussão, "
                                "cortante e perfurante. Se você for capaz de conjurar magias, você não poderá "
                                "conjurá-las ou se concentrar nelas enquanto estiver em fúria. Sua fúria dura por "
                                "1 minuto. Ela termina prematuramente se você cair inconsciente ou se seu turno acabar "
                                "e você não tiver atacado nenhuma criatura hostil desde seu último turno ou não tiver "
                                "sofrido dano nesse período. Você também pode terminar sua fúria no seu turno com uma "
                                "ação bônus. Quando você tiver usado a quantidade de fúrias mostrada para o seu nível "
                                "de bárbaro na coluna Fúrias da tabela O Bárbaro, você precisará terminar um descanso "
                                "longo antes de poder entrar em fúria novamente",
                       "DEFESA SEM ARMADURA": "Quando você não estiver vestindo qualquer armadura, sua Classe de "
                                              "Armadura será 10 + seu modificador de Destreza + seu modificador de "
                                              "Constituição. Você pode usar um escudo e continuar a receber esse "
                                              "benefício"}

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

        except Exception as e:
            print(e)

    def __get_name__(self):
        return self.name

    def __get_proficiency_bonus__(self):
        return self.proficiency_bonus

    def __get_life__(self):
        return self.life

    def __get_dices_life__(self):
        return self.dices_life

    def __get_knowledge__(self):
        return self.knowledge

    def __get_expertise__(self):
        return self.expertise

    def __get_equip__(self):
        return self.equip

    def __get_endurance_tests__(self):
        return self.endurance_tests

    def __get_skills__(self):
        return self.skills

    def __set_name__(self, vlr):
        self.name = vlr

    def __set_proficiency_bonus__(self, vlr):
        self.name = vlr

    def __set_life__(self, vlr):
        self.life = vlr

    def __set_dices_life__(self, vlr):
        self.dices_life = vlr

    def __set_knowledge__(self, vlr):
        self.knowledge.append(vlr)

    def __set_expertise__(self, vlr):
        self.expertise.append(vlr)

    def __set_endurance_tests__(self, vlr):
        self.endurance_tests.append(vlr)

    def __set_skills__(self, chave, vlr):
        self.skills[chave] = vlr

    def __set_config__(self, personagem):
        personagem.life += self.life
        for i in self.endurance_tests:
            personagem.dices["resistence_test"].append(i)
        personagem.proficiency_bonus = self.proficiency_bonus

        for n in self.knowledge:
            personagem.knowledge.append(n)

        for m in self.expertise:
            personagem.expertise.append(m)

        personagem.armor_class = 10 + personagem.dices['modifiers']["dexterity"] + personagem.dices['modifiers']["constitution"]
