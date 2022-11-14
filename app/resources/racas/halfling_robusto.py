from app.resources.racas.halfling import Halfling


class HalflingRobusto(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "HALFLING ROBUSTO"
        self.__sub_description__ = "Como um halfling pés-leves, você pode esconder-se facilmente, mesmo usando " \
                                   "apenas outras pessoas como cobertura. Você geralmente é afável e se dá muito " \
                                   "bem com os outros. Nos Reinos Esquecidos, os halflings pés-leves espalharam-se" \
                                   " até os lugares mais distantes e são a variedade mais comum. Pés-leves são mais" \
                                   " propensos à vontade de viajar do que os outros halflings, e muitas vezes vivem " \
                                   "ao lado deoutras raças ou levam uma vida nômade. No mundo de Greyhawk, estes" \
                                   " halflings são chamados pés-peludos ou companheiros altos."
        self.__add_skill__("Aumento no Valor de Habilidade", "Seu valor de Constituição aumenta em 1. ")
        self.__add_skill__("Resiliência dos Robustos. Você", "tem vantagem em testes de resistência contra veneno e"
                                                             " tem resistência contra dano de veneno. ")
        self.__set_constitution__(self.stats["constitution"] + 1)
    
    def __get_sub_description__(self):
        return self.__sub_description__
    
    def __set_sub_description__(self, sub_description):
        self.__sub_description__ = sub_description
