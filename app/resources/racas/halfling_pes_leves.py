from app.resources.racas.halfling import Halfling


class HalflingPesLeves(Halfling):
    def __init__(self, personagem):
        super().__init__()
        self.name = "HALFLING PÉS LEVES"
        self.__sub_description__ = "Como um halfling pés-leves, você pode esconder-se facilmente, mesmo usando " \
                                   "apenas outras pessoas como cobertura. Você geralmente é afável e se dá muito " \
                                   "bem com os outros. Nos Reinos Esquecidos, os halflings pés-leves espalharam-se " \
                                   "até os lugares mais distantes e são a variedade mais comum. Pés-leves são mais " \
                                   "propensos à vontade de viajar do que os outros halflings, e muitas vezes vivem " \
                                   "ao lado deoutras raças ou levam uma vida nômade. No mundo de Greyhawk, estes " \
                                   "halflings são chamados pés-peludos ou companheiros altos."
        self.__add_skill__("Aumento no Valor de Habilidade", "Seu valor de Carisma aumenta em 1. ")
        self.__add_skill__("Furtividade Natural", "Você pode tentar se esconder mesmo quando possuir apenas a "
                                                  "cobertura de uma criatura que for no mínimo um tamanho maior "
                                                  "que o seu.")
        self.__set_charisma__(self.stats["charisma"] + 2)
    
    def __get_sub_description__(self):
        return self.__sub_description__
    
    def __set_sub_description__(self, sub_description):
        self.__sub_description__ = sub_description
