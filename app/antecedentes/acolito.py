import random

from builders.Antecedente import Antecedente


class Acolito(Antecedente):
    def __init__(self):
        super().__init__()
        self.definer = ['Mercador De Guilda (Variant)',
                        'Alquimistas e boticários',
                        'Armeiros, chaveiros e ferreiros finos',
                        'Cervejeiros, destiladores e viticultores',
                        'Calígrafos, escribas e escrivães',
                        'Carpinteiros, construtores de telhado e estucadores',
                        'Cartógrafos, agrimensores e desenhistas',
                        'Remendões e sapateiros',
                        'Cozinheiros e padeiros',
                        'Vidraceiros e escultores',
                        'Joalheiros e lapidários',
                        'Coureiros, peleiros e curtidores',
                        'Pedreiros e marceneiros',
                        'Pintores, iluminadores e construtores de placas',
                        'Oleiros e telheiros',
                        'Armadores e veleiros',
                        'Ferreiros e forjadores',
                        'Funileiros, latoeiros e galheteiros',
                        'Fabricantes de carroças e fabricantes de rodas',
                        'Tecelões e tintureiros',
                        'Entalhadores, tanoeiros e construtores de arcos']
        self.personality_trait = ['Eu acredito que tudo que valha a pena fazer, vale a pena ser feito direito. Eu não '
                                  'posso evitar – Eu sou perfeccionista.',
                                  'Eu sou um esnobe que olha de cima a baixo aqueles que não sabem apreciar artes '
                                  'requintadas.',
                                  'Eu sempre quero aprender como as coisas funcionam e o que deixa as pessoas '
                                  'motivadas.',
                                  'Eu sou cheio de aforismos espirituosos e tenho um proverbio para cada ocasião. ',
                                  'Eu sou grosso com as pessoas que não tem o mesmo comprometimento que eu com o '
                                  'trabalho duro e honesto.',
                                  'Eu gosto de falar longamente sobre minha profissão.',
                                  'Eu não gasto meu dinheiro facilmente e vou barganhar incansavelmente para conseguir '
                                  'o melhor acordo possível.',
                                  'Eu sou bem conhecido pelo meu trabalho e quero ter certeza que todos o apreciam. '
                                  'Eu sempre fico surpreso '
                                  'quando conheço pessoas que não ouviram falar de mim.']
        self.ideal = ['Comunidade. É dever de todo cidadão civilizado fortalecer os elos da comunidade e a segurança '
                      'da civilização.',
                      'Generosidade. Meus talentos me foram dados para que eu pudesse usá-los para beneficiar o mundo. '
                      '(Bom)',
                      'Liberdade. Todos deveriam ser livres para perseguir seus próprios meios de vida. (Caótico)',
                      'Ganância. Eu só estou aqui pelo dinheiro. (Mau)',
                      'Povo. Eu sou cometido com o povo com quem me importo, não com ideias.',
                      'Aspiração. Eu trabaalho duro para ser o melhor no meu ofício.']
        self.bond = ['A oficina onde aprendi meu negócio é o local mais importante do mundo pra mim.',
                     'Eu criei um trabalho incrível para alguém, mas descobri que ele não era merecedor de recebê-lo. '
                     'Ainda estou à procura de alguém que seja merecedor.',
                     'Eu tenho uma grande dívida para com minha guilda por fazer de mim a pessoa que sou hoje.',
                     'Eu busco riqueza para conseguir o amor de alguém.',
                     'Um dia eu voltarei para a minha guilda e provarei que sou o maior artesão dentre eles.',
                     'Eu irem me vingar das forças malignas que destruíram meu local de negócios e arruinaram meu '
                     'estilo de vida.']
        self.flaw = ['Eu farei de tudo para pôr minha mãos em algo raro ou inestimável.',
                     'Eu rapidamente presumo que alguém está tentando me trapacear.',
                     'Ninguém nunca poderá saber que eu, certa vez, roubei dinheiro dos cofres da guilda.',
                     'Eu nunca estou satisfeito com o que tenho – eu sempre quero mais.',
                     'Eu mataria para adquirir um título de nobreza.',
                     'Eu sou terrivelmente invejoso com qualquer um que possa ofuscar meu ofício. Todo lugar que eu '
                     'vou, estou cercado de rivais.']

        self.background_format = Acolito.__set_background__(self)

    def __getattribute__(self, item):
        print(item)

    def __set_background__(self):
        self.background_format = {"type": Acolito.__set_type__(self),
                                  "personality_trait": Acolito.__set_personality_trait__(self),
                                  "ideal": Acolito.__set_ideal__(self),
                                  "bond": Acolito.__set_bond__(self),
                                  "flaw": Acolito.__set_ideal__(self)}

        return self.background_format

    def __set_type__(self):
        return random.choice(self.definer)

    def __set_personality_trait__(self):
        c1 = random.choice(self.personality_trait)
        self.personality_trait.remove(c1)
        c2 = random.choice(self.personality_trait)
        return [c1, c2]

    def __set_ideal__(self):
        return random.choice(self.ideal)

    def __set_bond__(self):
        return random.choice(self.bond)

    def __set_flaw__(self):
        return random.choice(self.flaw)
