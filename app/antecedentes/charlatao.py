import random

from builders.Antecedente import Antecedente


class Charlatao(Antecedente):
    def __init__(self, personagem):
        super().__init__()
        self.definer = ['Eu trapaceio em jogos de azar.',
                        'Eu falsifico moedas ou forjo documentos.',
                        'Eu me infiltro na vida das pessoas para descobrir suas fraquezas e ficar com suas fortunas.',
                        'Eu troco de identidade como troco de roupa.',
                        'Eu faço furtos rápidos nas esquinas das ruas.',
                        'Eu convenço as pessoas que tranqueiras inúteis valem seu suado dinheiro.']
        self.personality_trait = ['Eu me apaixono e desapaixono facilmente, e estou sempre em busca de alguém.',
                                  'Eu tenho uma piada para cada ocasião, especialmente ocasiões em que o humor é '
                                  'inapropriado.',
                                  'Bajulação é meu truque predileto para conseguir o que eu quero.',
                                  'Eu sou um jogador nato que não consegue resistir a se arriscar por uma possível '
                                  'ecompensa.',
                                  'Eu minto sobre quase tudo, mesmo quando não existe qualquer boa razão.',
                                  'Sarcasmo e insultos são minhas armas prediletas.',
                                  'Eu tenho vários símbolos sagrados comigo, e invoco a divindade que seja mais útil '
                                  'em cada '
                                  'dado momento.',
                                  'Eu furto qualquer coisa que eu vejo que possa ter algum valor.']
        self.ideal = ['Independência. Sou um espirito livre – ninguém me diz o que fazer.',
                      'Justiça. Eu nunca roubo de pessoas que não podem perder algumas moedas.',
                      'Caridade. Eu distribuo o dinheiro que adquiro com as pessoas que realmente precisam.',
                      'Criatividade. Eu nunca faço a mesma trapaça duas vezes.',
                      'Amizade. Bens materiais vem e vão. Os laços de amizade duram pra sempre.',
                      'Aspiração. Eu estou determinado a fazer algo por mim mesmo.']
        self. bond = ['Eu extorqui a pessoa errada e devo trabalhar para que esse indivíduo nunca mais cruze meu '
                      'caminho ou o das pessoas com quem me importo.',
                      'Eu devo tudo ao meu mentor – uma pessoa terrível que, provavelmente, está apodrecendo na cadeia '
                      'em algum lugar.',
                      'Em algum lugar por ai, eu tenho um filho que não me conhece. Eu estou tornando o mundo melhor '
                      'para ele.',
                      'Eu vim de uma família nobre e, um dia, irei reivindicar minhas terras e título daqueles que o '
                      'roubaram de mim.',
                      'Uma pessoa poderosa matou alguém que eu amava. Algum dia, em breve, terei minha vingança.',
                      'Eu enganei e arruinei a vida de uma pessoa que não merecia. Eu busco reparar meus erros, mas '
                      'talvez nunca seja capaz de me perdoar.']
        self.flaw = ['Não resisto um rostinho bonito.',
                     'Estou sempre com dividas. Eu gasto meus lucros ilícitos com luxurias decadentes mais rápido do '
                     'que os ganho...',
                     'Estou convencido que ninguém pode me enganar da forma que eu engano os outros.',
                     'Eu sou ganancioso demais pra meu próprio bem. Eu não consigo resistir a me arriscar se tiver '
                     'dinheiro envolvido.',
                     'Eu não resisto a enganar pessoas que são mais poderosas que eu.',
                     'Eu odeio admitir e vou me odiar por isso, mas, eu vou correr e salvar minha própria pele se as '
                     'coisas engrossarem.']

        personagem.background_format["name"] = "CHARLATÃO."
        personagem.background_format["type"] = Charlatao.bcgd_type(self)
        personagem.background_format["personality_trait"] = Charlatao.bcgd_personality_trait(self)
        personagem.background_format["ideal"] = Charlatao.bcgd_ideal(self)
        personagem.background_format["bond"] = Charlatao.bcgd_bond(self)
        personagem.background_format["flaw"] = Charlatao.bcgd_flaw(self)
        personagem.expertise.append('Enganação')
        personagem.expertise.append('Prestidigitação.')
        personagem.equip.append("Um conjunto de roupas finas.")
        personagem.equip.append("Um kit de disfarce.")
        personagem.equip.append("Ferramentas de trapaça.")
        personagem.equip.append("Á sua escolha: dez garrafas tampadas preenchidas com líquidos coloridos.")
        personagem.equip.append("Conjunto de dados viciados.")
        personagem.equip.append(random.choice(["Um baralho de cartas marcadas",
                                               "Um anel de sinete de um duque imaginário"]))
        personagem.equip.append("Algibeira.")
        personagem.knowledge.append("Kit de Disfarce.")
        personagem.knowledge.append("Kit de Falsificação.")
        personagem.knowledge.append("Característica: Identidade Falsa")
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
