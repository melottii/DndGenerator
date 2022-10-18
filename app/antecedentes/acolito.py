import random

from builders.Antecedente import Antecedente


class ArtesaoDeGuilda(Antecedente):
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

        self.background_format = ArtesaoDeGuilda.background_settings(self)

    def get_name(self):
        return "ANTECEDENTE: " + "ARTESÃO DE GUILDA"

    def get_type(self):
        return "VARIAÇÃO DO ANTECEDENTE: " + self.background_format["type"]

    def get_personality_trait(self):
        return f"TRAÇOS DE PERSONALIDADE 1: {self.background_format['personality_trait'][0]}\n"\
               f"TRAÇOS DE PERSONALIDADE 2: {self.background_format['personality_trait'][1]}"

    def get_ideal(self):
        return "IDEAL: " + self.background_format["ideal"]

    def get_bond(self):
        return "VINCULO: " + self.background_format["bond"]

    def get_flaw(self):
        return "DEFEITO: " + self.background_format["flaw"]

    def background_settings(self):
        self.background_format = {"type": ArtesaoDeGuilda.bcgd_type(self),
                                  "personality_trait": ArtesaoDeGuilda.bcgd_personality_trait(self),
                                  "ideal": ArtesaoDeGuilda.bcgd_ideal(self), "bond": ArtesaoDeGuilda.bcgd_bond(self),
                                  "flaw": ArtesaoDeGuilda.bcgd_flaw(self)}

        return self.background_format

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
