from app.builders.prototipo.Pacote import Pacote
from app.builders.prototipo.Equipamento import Equipamento


class Equipamentos:
    def __init__(self):
        self.pacotes = {"Pacote de Artista": {"preco": 40, "moeda": "po",
                                              "descricao": "Inclui uma mochila , um saco de dormir, duas fantasias, 5 "
                                                           "velas, 5 dias de rações, um cantil e um kit de disfarce.",
                                              "itens": [("Mochila", 1), ("Saco de dormir", 1), ("Fantasia", 2),
                                                        ("Rações de viagem (1 dia)", 5), ("Cantil", 1),
                                                        ("Kit de disfarce", 1)], },

                        "Pacote de Assaltante": {"preco": 16, "moeda": "po",
                                                 "descricao": "Inclui uma mochila, um saco com 1.000 esferas de metal,"
                                                              "3 metros de linha, um sino, 5 velas, um pé de cabra, um "
                                                              "martelo, 10 pítons , uma lanterna coberta, 2 frascos de "
                                                              "óleo, 5 dias de rações, uma caixa de fogo e um cantil. O"
                                                              " kit também possui 15 metros de corda de cânhamo "
                                                              "amarrada ao lado dele.",
                                                 "itens": [("Mochila", 1), ("Esferas (sacola com 1.000)", 1),
                                                           ("Linha (1 metro)", 3), ("Sino", 1), ("Vela", 5),
                                                           ("Pé de cabra", 1), ("Martelo", 1), ("Píton", 10),
                                                           ("Lanterna coberta", 1), ("Óleo (frasco)", 2),
                                                           ("Rações de viagem (1 dia)", 5), ("Caixa de fogo", 1),
                                                           ("Cantil", 1), ("Corda de cânhamo (15 metros)", 1)]},

                        "Pacote de Aventureiro": {"preco": 12, "moeda": "po",
                                                  "descricao": "Inclui uma mochila, um pé de cabra, um martelo, 10 "
                                                               "pítons, 10 tochas, uma caixa de fogo, 10 dias de rações"
                                                               " e um cantil. O kit também tem 15 metros de corda de "
                                                               "cânhamo amarrada ao"
                                                               " lado dele.",
                                                  "itens": [("Mochila", 1), ("Pé de cabra", 1), ("Píton", 10),
                                                            ("Tocha", 10), ("Caixa de fogo", 1),
                                                            ("Rações de viagem (1 dia)", 10),
                                                            ("Corda de cânhamo (15 metros)", 1)]},

                        "Pacote de Diplomata": {"preco": 39, "moeda": "po",
                                                "descricao": "Inclui um baú, 2 caixas para mapas ou pergaminhos, um "
                                                             "conjunto de roupas finas, um vidro de tinta , uma caneta"
                                                             " tinteiro, uma lâmpada, 2 frascos de óleo, 5 folhas de "
                                                             "papel, um vidro de perfume, parafina e sabão.",
                                                "itens": [("Baú", 1), ("Caixa para mapa ou pergaminho", 2),
                                                          ("Roupas finas", 1), ("Tinta (frasco de 30ml)", 1),
                                                          ("Caneta tinteiro", 1), ("Lâmpada", 1), ("Óleo (frasco)", 2),
                                                          ("Papel (uma folha)", 5), ("Perfume (frasco)", 1),
                                                          ("Parafina", 1), ("Sabão", 1)]},

                        "Pacote de Estudioso": {"preco": 40, "moeda": "po",
                                                "descricao": "Inclui uma mochila, um livro de estudo, um vidro de "
                                                             "tinta, uma caneta tinteiro, 10 folhas de pergaminho, um "
                                                             "saquinho de areia e uma pequena faca.",
                                                "itens": [("Mochila", 1), ("Livro", 1), ("Tinta (frasco de 30ml)", 1),
                                                          ("Caneta tinteiro", 1), ("Pergaminho (uma folha)", 10),
                                                          ("Saco", 1), ("Faca", 1)]},

                        "Pacote de Explorador": {"preco": 10, "moeda": "po",
                                                 "descricao": "Inclui uma mochila, um saco de dormir, um kit de "
                                                              "refeição, uma caixa de fogo, 10 tochas, 10 dias de "
                                                              "rações e um cantil. O kit também tem 15 metros de corda"
                                                              " de cânhamo amarrada ao lado dele.",
                                                 "itens": [("Mochila", 1), ("Saco de dormir", 1),
                                                           ("Kit de refeição", 1), ("Caixa de fogo", 1), ("Tocha", 10),
                                                           ("Rações de viagem (1 dia)", 10), ("Cantil", 1),
                                                           ("Corda de cânhamo (15 metros)", 1)]},

                        "Pacote de Sacerdote": {"preco": 19, "moeda": "po",
                                                "descricao": "Inclui uma mochila, um cobertor, 10 velas, uma caixa de "
                                                             "fogo, uma caixa de esmolas, 2 blocos de incenso, um "
                                                             "incensário, vestes, 2 dias de rações e um cantil.",
                                                "itens": [("Mochila", 1), ("Cobertor de inverno", 1), ("Vela", 10),
                                                          ("Caixa de fogo", 1), ("Caixa de esmola", 1),
                                                          ("Bloco de incenso", 2), ("Incensário", 1),
                                                          ("Roupas comuns ", 1), ("Rações de viagem (1 dia)", 2),
                                                          ("Cantil", 1)]}}

        self.equipamentos = {"Aljava": {"preco": 1, "moeda": "po", "peso": 0.5},
                             "Flechas (20)": {"preco": 1, "moeda": "po", "peso": 0.5},
                             "Mochila": {"preco": 2, "moeda": "po", "peso": 2.5},
                             "Saco de dormir": {"preco": 1, "moeda": "po", "peso": 3.5},
                             "Fantasia": {"preco": 1, "moeda": "po", "peso": 0},
                             "Rações de viagem (1 dia)": {"preco": 5, "moeda": "pp", "peso": 1},
                             "Cantil": {"preco": 2, "moeda": "pp", "peso": 2.5},
                             "Kit de disfarce": {"preco": 25, "moeda": "po", "peso": 1.5},
                             "Esferas (sacola com 1.000)": {"preco": 1, "moeda": "po", "peso": 1},
                             "Linha (1 metro)": {"preco": 1, "moeda": "po", "peso": 0},
                             "Sino": {"preco": 1, "moeda": "po", "peso": 0},
                             "Vela": {"preco": 1, "moeda": "pc", "peso": 0},
                             "Livro": {"preco": 25, "moeda": "po", "peso": 2.5},
                             "Pé de cabra": {"preco": 2, "moeda": "po", "peso": 2.5},
                             "Martelo": {"preco": 1, "moeda": "po", "peso": 1.5},
                             "Píton": {"preco": 5, "moeda": "pc", "peso": 0},
                             "Lanterna coberta": {"preco": 5, "moeda": "po", "peso": 1},
                             "Caixa de fogo": {"preco": 5, "moeda": "pp", "peso": 0.5},
                             "Corda de cânhamo (15 metros)": {"preco": 1, "moeda": "po", "peso": 5},
                             "Tocha": {"preco": 1, "moeda": "pc", "peso": 0.5},
                             "Baú": {"preco": 5, "moeda": "po", "peso": 12.5},
                             "Caixa para mapa ou pergaminho": {"preco": 1, "moeda": "po", "peso": 0},
                             "Roupas finas": {"preco": 15, "moeda": "po", "peso": 3},
                             "Caneta tinteiro": {"preco": 2, "moeda": "pc", "peso": 0},
                             "Lâmpada": {"preco": 5, "moeda": "pp", "peso": 0.5},
                             "Óleo (frasco)": {"preco": 1, "moeda": "pp", "peso": 0.5},
                             "Papel (uma folha)": {"preco": 2, "moeda": "pp", "peso": 0},
                             "Perfume (frasco)": {"preco": 5, "moeda": "po", "peso": 0},
                             "Parafina": {"preco": 5, "moeda": "pp", "peso": 0},
                             "Sabão": {"preco": 2, "moeda": "pc", "peso": 0},
                             "Tinta (frasco de 30ml)": {"preco": 10, "moeda": "po", "peso": 0},
                             "Pergaminho (uma folha)": {"preco": 1, "moeda": "pp", "peso": 0},
                             "Saco": {"preco": 1, "moeda": "pc", "peso": 0.25},
                             "Faca": {"preco": 1, "moeda": "pp", "peso": 0},
                             "Kit de refeição": {"preco": 1, "moeda": "po", "peso": 0},
                             "Cobertor de inverno": {"preco": 5, "moeda": "pp", "peso": 1.5},
                             "Caixa de esmola": {"preco": 5, "moeda": "pp", "peso": 0.5},
                             "Bloco de incenso": {"preco": 1, "moeda": "pp", "peso": 0},
                             "Incensário": {"preco": 1, "moeda": "pp", "peso": 0},
                             "Roupas comuns": {"preco": 5, "moeda": "pp", "peso": 1.5},
                             "Símbolo sagrado": {"preco": 0, "moeda": "pp", "peso": 0},
                             "Livro de preces": {"preco": 25, "moeda": "po", "peso": 2.5},
                             "Conta de orações": {"preco": 25, "moeda": "po", "peso": 2.5},
                             "Vareta de incenso": {"preco": 1, "moeda": "pp", "peso": 0},
                             "Vestimenta de acólito": {"preco": 0, "moeda": "pp", "peso": 0},
                             "Algibeira": {"preco": 5, "moeda": "po", "peso": 0.5},
                             "Ferramentas de carpinteiro": {"preco": 8, "moeda": "po", "peso": 3},
                             "Ferramentas de cartógrafo": {"preco": 15, "moeda": "po", "peso": 3},
                             "Ferramentas de costureiro": {"preco": 1, "moeda": "po", "peso": 2.5},
                             "Ferramentas de coureiro": {"preco": 5, "moeda": "po", "peso": 2.5},
                             "Ferramentas de entalhador": {"preco": 1, "moeda": "po", "peso": 2.5},
                             "Ferramentas de ferreiro": {"preco": 20, "moeda": "po", "peso": 4},
                             "Ferramentas de funileiro": {"preco": 50, "moeda": "po", "peso": 5},
                             "Ferramentas de joalheiro": {"preco": 25, "moeda": "po", "peso": 1},
                             "Ferramentas de oleiro": {"preco": 10, "moeda": "po", "peso": 1.5},
                             "Ferramentas de pedreiro": {"preco": 10, "moeda": "po", "peso": 4},
                             "Ferramentas de pintor": {"preco": 10, "moeda": "po", "peso": 2.5},
                             "Ferramentas de sapateiro": {"preco": 5, "moeda": "po", "peso": 2.5},
                             "Ferramentas de vidreiro": {"preco": 30, "moeda": "po", "peso": 2.5},
                             "Suprimentos de alquimista": {"preco": 50, "moeda": "po", "peso": 4},
                             "Suprimentos de cervejeiro": {"preco": 20, "moeda": "po", "peso": 4.5},
                             "Suprimentos de caligrafia": {"preco": 10, "moeda": "po", "peso": 2.5},
                             "Ferramentas de trapaça": {"preco": 1, "moeda": "po", "peso": 2.5},
                             "Utensílios de cozinheiro": {"preco": 1, "moeda": "po", "peso": 4},
                             "Carta de apresentação da guilda": {"preco": 0, "moeda": "po", "peso": 0},
                             "Roupas de viajante": {"preco": 2, "moeda": "po", "peso": 2},
                             "Baralho de cartas marcadas": {"preco": 5, "moeda": "pp", "peso": 0},
                             "Anel de sinete de um duque imaginário": {"preco": 0, "moeda": "pp", "peso": 0},
                             "Conjunto de dados viciados": {"preco": 1, "moeda": "pp", "peso": 0},
                             "Garrafa de vidro tampada com líquido colorido": {"preco": 1, "moeda": "po", "peso": 1},
                             "Ferramentas de ladrão": {"preco": 25, "moeda": "po", "peso": 0.5},
                             "Virotes (20)": {"preco": 1, "moeda": "po", "peso": 0.75},
                             "Bolsa de componentes": {"preco": 25, "moeda": "po", "peso": 1},
                             "Bastão": {"preco": 10, "moeda": "po", "peso": 1},
                             "Cajado": {"preco": 5, "moeda": "po", "peso": 2},
                             "Cristal": {"preco": 10, "moeda": "po", "peso": 0.5},
                             "Orbe": {"preco": 20, "moeda": "po", "peso": 1.5},
                             "Varinha": {"preco": 10, "moeda": "po", "peso": 0.5}, }

    def __set_pacote__(self, pacote, attb):
        self.pacotes[pacote] = attb

    def __get_pacote__(self, pacote):
        return {pacote: self.pacotes[pacote]}

    def __get_pacote_list__(self):
        return [i for i in self.pacotes.keys()]

    def __set_equipamento__(self, equipamento, attb):
        self.equipamentos[equipamento] = attb

    def __get_equipamento__(self, equipamento):
        return {equipamento: self.equipamentos[equipamento]}

    def __clone_pacote__(self, pacote_dict):
        itens = []
        for pacote in pacote_dict:
            for item, quant in pacote_dict[pacote]["itens"]:
                item_dict = self.__get_equipamento__(item)
                item_obj = self.__clone_equipamento__(item_dict)
                item_obj.__set_quantidade__(quant)
                itens.append(item_obj)
            pacote_obj = Pacote(pacote, pacote_dict[pacote]["preco"], pacote_dict[pacote]["moeda"], itens)
            return pacote_obj

    @staticmethod
    def __clone_equipamento__(equipamento_dict, quant=1):
        for equipamento in equipamento_dict:
            equipamento_obj = Equipamento(equipamento, equipamento_dict[equipamento]["preco"],
                                          equipamento_dict[equipamento]["moeda"], equipamento_dict[equipamento]["peso"],
                                          quant)
            return equipamento_obj
