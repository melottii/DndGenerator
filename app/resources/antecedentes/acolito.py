import random

from app.builders.Antecedente import Antecedente


class Acolito(Antecedente):
    def __init__(self, personagem):
        super().__init__()
        self.definer = ['Acólito sem variação.']
        self.personality_trait = ['Eu idolatro um herói particular da minha fé, e constantemente me refiro a seus '
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
        self.ideal = ['Tradição. As tradições ancestrais de adoração e sacrifício devem ser preservadas e perpetradas',
                      'Caridade. Eu sempre tento ajudar aqueles em necessidade, não importando o custo pessoal.',
                      'Mudança. Nós devemos ajudar a conduzir as mudanças que os deuses estão constantemente '
                      'trabalhando para o mundo.',
                      'Poder. Eu espero que um dia eu consiga chegar ao topo na hierarquia da minha religião.',
                      'Fé. Eu acredito que minha divindade guia minhas ações. Eu tenho fé que, se eu trabalhar duro, '
                      'coisas boas acontecerão.',
                      'Aspiração. Eu busco ser digno da graça do meu deus ao corresponder minhas ações aos seus '
                      'ensinamentos.']
        self.bond = ['Eu morreria para recuperar uma relíquia ancestral de minha fé, perdida há muito tempo.',
                     'Eu ainda terei minha vingança contra o templo corrupto que me acusou de heresia.',
                     'Eu devo minha vida ao sacerdote que me acolheu quando meus pais morreram.',
                     'Tudo o que faço, faço pelo povo.',
                     'Eu farei qualquer coisa para proteger o templo que sirvo.',
                     'Eu busco guardar um texto sagrado que meus inimigos dizem ser herético e tentam destruí-lo.']
        self.flaw = ['Eu julgo os outros severamente, e a mim mesmo mais ainda.',
                     'Eu deposito muita confiança naqueles que detêm o poder na hierarquia de meu templo.',
                     'Minha devoção é muitas vezes me cega perante aqueles que professam a fé do meu deus.',
                     'Meu pensamento é inflexível.',
                     'Eu suspeito de estranhos e sempre espero o pior deles.',
                     'Depois de escolher um objetivo, eu fico obcecado em cumpri-lo, até mesmo em detrimento de '
                     'qualquer outra coisa em minha vida.']

        personagem.background_format["name"] = "ACÓLITO."
        personagem.background_format["type"] = Acolito.bcgd_type(self)
        personagem.background_format["personality_trait"] = Acolito.bcgd_personality_trait(self)
        personagem.background_format["ideal"] = Acolito.bcgd_ideal(self)
        personagem.background_format["bond"] = Acolito.bcgd_bond(self)
        personagem.background_format["flaw"] = Acolito.bcgd_flaw(self)
        personagem.expertise.append('Intuição')
        personagem.expertise.append('Religião')
        personagem.idiom["rand"] += 2
        personagem.equip.append("Um símbolo sagrado (um presente dado quando você entrou no templo).")
        personagem.equip.append("Livro de preces ou uma conta de orações.")
        personagem.equip.append("5 varetas de incenso.")
        personagem.equip.append("Vestimentas de acólito.")
        personagem.equip.append("Conjunto de roupas comuns.")
        personagem.equip.append("Algibeira.")
        personagem.knowledge.append("Característica: Abrigo dos fiéis")
        personagem.money["ouro (po)"] += 15

    def get_name(self, personagem):
        return "ANTECEDENTE: " + personagem.background_format["name"]

    def get_type(self, personagem):
        return "VARIAÇÃO DO ANTECEDENTE: " + personagem.background_format["type"]

    def get_personality_trait(self, personagem):
        return f"TRAÇOS DE PERSONALIDADE 1: {personagem.background_format['personality_trait'][0]}\n" \
               f"TRAÇOS DE PERSONALIDADE 2: {personagem.background_format['personality_trait'][1]}"

    def get_ideal(self, personagem):
        return "IDEAL: " + personagem.background_format["ideal"]

    def get_bond(self, personagem):
        return "VINCULO: " + personagem.background_format["bond"]

    def get_flaw(self, personagem):
        return "DEFEITO: " + personagem.background_format["flaw"]

    def bcgd_type(self):
        return random.choice(self.definer)

    def bcgd_personality_trait(self):
        c1 = random.choice(self.personality_trait)
        self.personality_trait.remove(c1)
        c2 = random.choice(self.personality_trait)
        return [c1, c2]

    def bcgd_ideal(self):
        return random.choice(self.ideal)

    def bcgd_bond(self):
        return random.choice(self.bond)

    def bcgd_flaw(self):
        return random.choice(self.flaw)
