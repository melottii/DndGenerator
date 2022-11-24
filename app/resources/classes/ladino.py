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
        self.skills = {"ESPECIALIZAÇÃO": "No 1º nível, você escolhe duas de suas perícias que seja proficiente, ou uma "
                                         "perícia que seja proficiente e ferramentas de ladrão. Seu bônus de "
                                         "proficiência é dobrado em qualquer teste de habilidade que fizer com elas. "
                                         "No 6º nível, você pode escolher outras duas de suas proficiências (em "
                                         "perícias ou ferramentas de ladrão) para ganhar esse benefício.",
                       "ATAQUE FURTIVO": "A partir do 1º nível, você sabe como atacar sutilmente e explorar a distração"
                                         " de seus inimigos. Uma vez por turno, você pode adicionar 1d6 nas jogadas de"
                                         " dano contra qualquer criatura que acertar, desde que tenha vantagem nas "
                                         "jogadas de ataque. O ataque deve ser com uma arma de acuidade ou à distância."
                                         " Você não precisa ter vantagem nas jogadas de ataque se outro inimigo do seu"
                                         " alvo estiver a 1,5 metro de distância dele, desde que este inimigo não "
                                         "esteja incapacitado e você não tenha desvantagem nas jogadas de ataque. A"
                                         " quantidade de dano extra aumenta conforme você ganha níveis nessa classe,"
                                         " como mostrado na coluna Ataque Furtivo da tabela O Ladino.",
                       "GÍRIA DE LADRÃO": "Durante seu treinamento você aprendeu as gírias de ladrão, um misto de "
                                          "dialeto, jargão e códigos secretos que permitem você passar mensagens "
                                          "secretas durante uma conversa aparentemente normal. Somente outra criatura"
                                          " que conheça essas gírias de ladrão entende as mensagens. Leva-se quatro "
                                          "vezes mais tempo para transmitir essa mensagem do que falar a mesma ideia"
                                          " claramente. Além disso, você entende um conjunto de sinais secretos e "
                                          "símbolos usados para transmitir mensagens curtas e simples, como saber se"
                                          " uma área é perigosa ou se é território de uma guilda de ladrões, se o "
                                          "saque está próximo, se as pessoas na área são alvos fáceis ou até mesmo"
                                          " indicar lugares seguros para ladinos se esconderem."}

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
