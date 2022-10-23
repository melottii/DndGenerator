import random

from app.builders.Antecedente import Antecedente


class Acolito(Antecedente):
    def __init__(self, personagem):
        super().__init__()
        self.equips = ["Um símbolo sagrado (um presente dado quando você entrou no templo).",
                       "Livro de preces ou uma conta de orações.",
                       "5 varetas de incenso.",
                       "Vestimentas de acólito.",
                       "Conjunto de roupas comuns.",
                       "Algibeira."]
        self.idiom = {"rand": 2}
        self.expertise = ['Intuição', 'Religião']
        self.knowledge = ["Característica: Abrigo dos fiéis"]
        self.money = {"ouro (po)": 15}
        self.background_format = {"name": "ACÓLITO.",
                                  "type": Acolito.__set_type__(),
                                  "personality_trait": Acolito.__set_personalityTrait__(),
                                  "ideal": Acolito.__set_ideal__(),
                                  "bond": Acolito.__set_bond__(),
                                  "flaw": Acolito.__set_flaw__()}

        Acolito.__set_config__(self, personagem)

    def __get_name__(self, **kwargs):
        return "ANTECEDENTE: " + self.background_format["name"]

    def __get_type__(self, **kwargs):
        return "VARIAÇÃO DO ANTECEDENTE: " + self.background_format["type"]

    def __get_personalityTrait__(self, **kwargs):
        return f"TRAÇOS DE PERSONALIDADE 1: {self.background_format['personality_trait'][0]}\n" \
               f"TRAÇOS DE PERSONALIDADE 2: {self.background_format['personality_trait'][1]}"

    def __get_ideal__(self, **kwargs):
        return "IDEAL: " + self.background_format["ideal"]

    def __get_bond__(self, **kwargs):
        return "VINCULO: " + self.background_format["bond"]

    def __get_flaw__(self, **kwargs):
        return "DEFEITO: " + self.background_format["flaw"]

    @staticmethod
    def __set_type__():
        definer = ['Acólito sem variação.']
        return random.choice(definer)

    @staticmethod
    def __set_personalityTrait__():
        personality_trait = ['Eu idolatro um herói particular da minha fé, e constantemente me refiro a seus '
                             'feitos e exemplos.',
                             'Eu consigo encontrar semelhanças mesmo entre os inimigos mais violentos, com empatia'
                             ' e sempre trabalhando pela paz. ',
                             'Eu vejo presságios em cada evento e ação. Os deuses estão falando conosco, nós '
                             'apenas temos de ouvi-los.',
                             'Nada pode abalar minha atitude otimista.',
                             'Eu cito (corretamente ou não) textos sagrados e provérbios em quase qualquer '
                             'situação.',
                             'Eu sou tolerante (ou intolerante) a qualquer outra fé, e respeito (ou condeno) a '
                             'adoração a outros deuses.',
                             'Eu aprecio comida requintada, bebidas e a elite entre o alto escalão de meu templo. '
                             'Uma vida dura me irrita.',
                             'Eu passei tanto tempo no templo que possuo pouca prática em lidar com as pessoas '
                             'mundo a fora.']
        c1 = random.choice(personality_trait)
        personality_trait.remove(c1)
        c2 = random.choice(personality_trait)
        return [c1, c2]

    @staticmethod
    def __set_ideal__():
        ideal = ['Tradição. As tradições ancestrais de adoração e sacrifício devem ser preservadas e perpetradas',
                 'Caridade. Eu sempre tento ajudar aqueles em necessidade, não importando o custo pessoal.',
                 'Mudança. Nós devemos ajudar a conduzir as mudanças que os deuses estão constantemente '
                 'trabalhando para o mundo.',
                 'Poder. Eu espero que um dia eu consiga chegar ao topo na hierarquia da minha religião.',
                 'Fé. Eu acredito que minha divindade guia minhas ações. Eu tenho fé que, se eu trabalhar duro, '
                 'coisas boas acontecerão.',
                 'Aspiração. Eu busco ser digno da graça do meu deus ao corresponder minhas ações aos seus '
                 'ensinamentos.']
        return random.choice(ideal)

    @staticmethod
    def __set_bond__():
        bond = ['Eu morreria para recuperar uma relíquia ancestral de minha fé, perdida há muito tempo.',
                'Eu ainda terei minha vingança contra o templo corrupto que me acusou de heresia.',
                'Eu devo minha vida ao sacerdote que me acolheu quando meus pais morreram.',
                'Tudo o que faço, faço pelo povo.',
                'Eu farei qualquer coisa para proteger o templo que sirvo.',
                'Eu busco guardar um texto sagrado que meus inimigos dizem ser herético e tentam destruí-lo.']
        return random.choice(bond)

    @staticmethod
    def __set_flaw__():
        flaw = ['Eu julgo os outros severamente, e a mim mesmo mais ainda.',
                'Eu deposito muita confiança naqueles que detêm o poder na hierarquia de meu templo.',
                'Minha devoção é muitas vezes me cega perante aqueles que professam a fé do meu deus.',
                'Meu pensamento é inflexível.',
                'Eu suspeito de estranhos e sempre espero o pior deles.',
                'Depois de escolher um objetivo, eu fico obcecado em cumpri-lo, até mesmo em detrimento de '
                'qualquer outra coisa em minha vida.']
        return random.choice(flaw)

    def __set_config__(self, personagem):
        for equip in self.equips:
            personagem.equip.append(equip)
        for exp in self.expertise:
            personagem.expertise.append(exp)
        for know in self.knowledge:
            personagem.knowledge.append(know)
        for gold in self.money:
            personagem.money[gold] += self.money[gold]
        personagem.idiom["rand"] = self.idiom["rand"]
