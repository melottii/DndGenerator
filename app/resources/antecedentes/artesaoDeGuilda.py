import random

from app.builders.Antecedente import Antecedente


class ArtesaoDeGuilda(Antecedente):
    def __init__(self, personagem):
        super().__init__()
        self.equips = ["Conjunto de ferramentas de artesão"
                       "Carta de apresentação da sua guilda"
                       "Conjunto de roupas de viajante", "Uma algibeira"]
        self.idiom = {"rand": 1}
        self.expertise = ['Intuição', 'Persuasão']
        self.knowledge = ["Característica: Abrigo dos fiéis"]
        self.money = {"ouro (po)": 15}
        self.background_format = {"name": "ARTESÃO DE GUILDA",
                                  "type": ArtesaoDeGuilda.__set_type__(),
                                  "personality_trait": ArtesaoDeGuilda.__set_personalityTrait__(),
                                  "ideal": ArtesaoDeGuilda.__set_ideal__(),
                                  "bond": ArtesaoDeGuilda.__set_bond__(),
                                  "flaw": ArtesaoDeGuilda.__set_flaw__()}
        ArtesaoDeGuilda.__set_config__(self, personagem)

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
        definer = ['Mercador De Guilda (Variant)', 'Alquimistas e boticários', 'Armeiros, chaveiros e ferreiros finos',
                   'Cervejeiros, destiladores e viticultores', 'Calígrafos, escribas e escrivães',
                   'Carpinteiros, construtores de telhado e estucadores', 'Cartógrafos, agrimensores e desenhistas',
                   'Remendões e sapateiros', 'Cozinheiros e padeiros', 'Vidraceiros e escultores',
                   'Joalheiros e lapidários', 'Coureiros, peleiros e curtidores', 'Pedreiros e marceneiros',
                   'Pintores, iluminadores e construtores de placas', 'Oleiros e telheiros', 'Armadores e veleiros',
                   'Ferreiros e forjadores', 'Funileiros, latoeiros e galheteiros',
                   'Fabricantes de carroças e fabricantes de rodas', 'Tecelões e tintureiros',
                   'Entalhadores, tanoeiros e construtores de arcos']
        return random.choice(definer)

    @staticmethod
    def __set_personalityTrait__():
        personality_trait = ['Eu acredito que tudo que valha a pena fazer, vale a pena ser feito direito. Eu não '
                             'posso evitar – Eu sou perfeccionista.',
                             'Eu sou um esnobe que olha de cima a baixo aqueles que não sabem apreciar artes '
                             'requintadas.',
                             'Eu sempre quero aprender como as coisas funcionam e o que deixa as pessoas '
                             'motivadas.',
                             'Eu sou cheio de aforismos espirituosos e tenho um proverbio para cada ocasião. ',
                             'Eu sou grosso com as pessoas que não tem o mesmo comprometimento que eu com o '
                             'trabalho duro e honesto.', 'Eu gosto de falar longamente sobre minha profissão.',
                             'Eu não gasto meu dinheiro facilmente e vou barganhar incansavelmente para conseguir '
                             'o melhor acordo possível.',
                             'Eu sou bem conhecido pelo meu trabalho e quero ter certeza que todos o apreciam. '
                             'Eu sempre fico surpreso '
                             'quando conheço pessoas que não ouviram falar de mim.']
        c1 = random.choice(personality_trait)
        personality_trait.remove(c1)
        c2 = random.choice(personality_trait)
        return [c1, c2]

    @staticmethod
    def __set_ideal__():
        ideal = ['Comunidade. É dever de todo cidadão civilizado fortalecer os elos da comunidade e a segurança '
                 'da civilização.',
                 'Generosidade. Meus talentos me foram dados para que eu pudesse usá-los para beneficiar o mundo. '
                 '(Bom)', 'Liberdade. Todos deveriam ser livres para perseguir seus próprios meios de vida. (Caótico)',
                 'Ganância. Eu só estou aqui pelo dinheiro. (Mau)',
                 'Povo. Eu sou cometido com o povo com quem me importo, não com ideias.',
                 'Aspiração. Eu trabaalho duro para ser o melhor no meu ofício.']
        return random.choice(ideal)

    @staticmethod
    def __set_bond__():
        bond = ['A oficina onde aprendi meu negócio é o local mais importante do mundo pra mim.',
                'Eu criei um trabalho incrível para alguém, mas descobri que ele não era merecedor de recebê-lo. '
                'Ainda estou à procura de alguém que seja merecedor.',
                'Eu tenho uma grande dívida para com minha guilda por fazer de mim a pessoa que sou hoje.',
                'Eu busco riqueza para conseguir o amor de alguém.',
                'Um dia eu voltarei para a minha guilda e provarei que sou o maior artesão dentre eles.',
                'Eu irem me vingar das forças malignas que destruíram meu local de negócios e arruinaram meu '
                'estilo de vida.']
        return random.choice(bond)

    @staticmethod
    def __set_flaw__():
        flaw = ['Eu farei de tudo para pôr minha mãos em algo raro ou inestimável.',
                'Eu rapidamente presumo que alguém está tentando me trapacear.',
                'Ninguém nunca poderá saber que eu, certa vez, roubei dinheiro dos cofres da guilda.',
                'Eu nunca estou satisfeito com o que tenho – eu sempre quero mais.',
                'Eu mataria para adquirir um título de nobreza.',
                'Eu sou terrivelmente invejoso com qualquer um que possa ofuscar meu ofício. Todo lugar que eu '
                'vou, estou cercado de rivais.']
        return random.choice(flaw)

    def __set_config__(self, personagem):
        for equip in self.equips:
            personagem.equip["Equipamentos"].append(equip)
        for exp in self.expertise:
            personagem.expertise.append(exp)
        for know in self.knowledge:
            personagem.knowledge.append(know)
        for gold in self.money:
            personagem.money[gold] += self.money[gold]
        personagem.idiom["rand"] = self.idiom["rand"]
