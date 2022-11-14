import random

from app.builders.fabrica_abstrata.Antecedente import Antecedente
from app.builders.prototipo.ItemPrototipo import ItemPrototipo

class Charlatao(Antecedente):
    def __init__(self, personagem):
        super().__init__()
        self.idiom = {"rand": 1}
        self.expertise = ['Enganação', 'Prestidigitação']
        self.knowledge = ["Kit de Disfarce.", "Kit de Falsificação", "Característica: Identidade Falsa"]
        self.money = {"ouro (po)": 15}

        self.background_format = {"name": "CHARLATÃO",
                                  "type": Charlatao.__set_type__(),
                                  "personality_trait": Charlatao.__set_personalityTrait__(),
                                  "ideal": Charlatao.__set_ideal__(),
                                  "bond": Charlatao.__set_bond__(),
                                  "flaw": Charlatao.__set_flaw__()}

        Charlatao.__set_config__(self, personagem)

    @staticmethod
    def __get_name__(self, **kwargs):
        return "ANTECEDENTE: " + self.background_format["name"]

    @staticmethod
    def __get_type__(self, **kwargs):
        return "VARIAÇÃO DO ANTECEDENTE: " + self.background_format["type"]

    @staticmethod
    def __get_personalityTrait__(self, **kwargs):
        return f"TRAÇOS DE PERSONALIDADE 1: {self.background_format['personality_trait'][0]}\n" \
               f"TRAÇOS DE PERSONALIDADE 2: {self.background_format['personality_trait'][1]}"

    @staticmethod
    def __get_ideal__(self, **kwargs):
        return "IDEAL: " + self.background_format["ideal"]

    @staticmethod
    def __get_bond__(self, **kwargs):
        return "VINCULO: " + self.background_format["bond"]

    def __get_flaw__(self, **kwargs):
        return "DEFEITO: " + self.background_format["flaw"]

    @staticmethod
    def __set_type__():
        definer = ['Eu trapaceio em jogos de azar.',
                   'Eu falsifico moedas ou forjo documentos.',
                   'Eu me infiltro na vida das pessoas para descobrir suas fraquezas e ficar com suas fortunas.',
                   'Eu troco de identidade como troco de roupa.',
                   'Eu faço furtos rápidos nas esquinas das ruas.',
                   'Eu convenço as pessoas que tranqueiras inúteis valem seu suado dinheiro.']
        return random.choice(definer)

    @staticmethod
    def __set_personalityTrait__():
        personality_trait = ['Eu me apaixono e desapaixono facilmente, e estou sempre em busca de alguém.',
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
        c1 = random.choice(personality_trait)
        personality_trait.remove(c1)
        c2 = random.choice(personality_trait)
        return [c1, c2]

    @staticmethod
    def __set_ideal__():
        ideal = ['Independência. Sou um espirito livre – ninguém me diz o que fazer.',
                 'Justiça. Eu nunca roubo de pessoas que não podem perder algumas moedas.',
                 'Caridade. Eu distribuo o dinheiro que adquiro com as pessoas que realmente precisam.',
                 'Criatividade. Eu nunca faço a mesma trapaça duas vezes.',
                 'Amizade. Bens materiais vem e vão. Os laços de amizade duram pra sempre.',
                 'Aspiração. Eu estou determinado a fazer algo por mim mesmo.']
        return random.choice(ideal)

    @staticmethod
    def __set_bond__():
        bond = ['Eu extorqui a pessoa errada e devo trabalhar para que esse indivíduo nunca mais cruze meu '
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
        return random.choice(bond)

    @staticmethod
    def __set_flaw__():
        flaw = ['Não resisto um rostinho bonito.',
                'Estou sempre com dividas. Eu gasto meus lucros ilícitos com luxurias decadentes mais rápido do '
                'que os ganho...',
                'Estou convencido que ninguém pode me enganar da forma que eu engano os outros.',
                'Eu sou ganancioso demais pra meu próprio bem. Eu não consigo resistir a me arriscar se tiver '
                'dinheiro envolvido.',
                'Eu não resisto a enganar pessoas que são mais poderosas que eu.',
                'Eu odeio admitir e vou me odiar por isso, mas, eu vou correr e salvar minha própria pele se as '
                'coisas engrossarem.']
        return random.choice(flaw)
    
    def __set_equips__(self, personagem):
        nome = random.choice(["Baralho de cartas marcadas","Anel de sinete de um duque imaginário" ])
        equip = ItemPrototipo().get_equipamento(nome, 1)
        personagem.equip["Equipamentos"].append(equip)
    
        equip = ItemPrototipo().get_equipamento("Roupas finas", 1)
        personagem.equip["Equipamentos"].append(equip)

        equip = ItemPrototipo().get_equipamento("Kit de disfarce", 1)
        personagem.equip["Equipamentos"].append(equip)

        equip = ItemPrototipo().get_equipamento("Ferramentas de trapaça", 1)
        personagem.equip["Equipamentos"].append(equip)
    
        equip = ItemPrototipo().get_equipamento("Garrafa de vidro tampada com líquido colorido", 10)
        personagem.equip["Equipamentos"].append(equip)

        equip = ItemPrototipo().get_equipamento("Conjunto de dados viciados", 1)
        personagem.equip["Equipamentos"].append(equip)

        equip = ItemPrototipo().get_equipamento("Algibeira", 1)
        personagem.equip["Equipamentos"].append(equip)

    def __set_config__(self, personagem):
        self.__set_equips__(personagem)

        for exp in self.expertise:
            personagem.expertise.append(exp)
        for know in self.knowledge:
            personagem.knowledge.append(know)
        for gold in self.money:
            personagem.money[gold] += self.money[gold]
        personagem.idiom["rand"] = self.idiom["rand"]
