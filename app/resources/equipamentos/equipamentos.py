class Equipamentos:
    def __init__(self):
        self.pacotes = {"Pacote de Artista": ["Valor do pacote: 40 po",
                                              "Inclui uma mochila , um saco de dormir, duas fantasias, 5 velas, "
                                              "5 dias de rações, um cantil e um kit de disfarce."],
                        "Pacote de Assaltante": ["Valor do pacote: 16 po",
                                                 "Inclui uma mochila, um saco com 1.000 esferas de metal, 3 "
                                                 "metros de linha, um sino, 5 velas, um pé de cabra, um "
                                                 "martelo, 10 pítons , uma lanterna coberta, 2 frascos de óleo,"
                                                 " 5 dias de rações, uma caixa de fogo e um cantil. O kit "
                                                 "também possui 15 metros de corda de cânhamo amarrada ao lado "
                                                 "dele."],
                        "Pacote de Aventureiro": ["Valor do pacote: 12 po",
                                                  "Inclui uma mochila, um pé de cabra, um martelo, 10 pítons, "
                                                  "10 tochas, uma caixa de fogo, 10 dias de rações e um cantil."
                                                  " O kit também tem 15 metros de corda de cânhamo amarrada ao"
                                                  " lado dele."],
                        "Pacote de Diplomata": ["Valor do pacote: 39 po",
                                                "Inclui um baú, 2 caixas para mapas ou pergaminhos, um conjunto"
                                                " de roupas finas, um vidro de tinta , uma caneta tinteiro, uma"
                                                " lâmpada, 2 frascos de óleo, 5 folhas de papel, um vidro de "
                                                "perfume, parafina e sabão."],
                        "Pacote de Estudioso": ["Valor do pacote: 40 po",
                                                "Inclui uma mochila, um livro de estudo, um vidro de tinta, uma"
                                                " caneta tinteiro, 10 folhas de pergaminho, um saquinho de "
                                                "areia e uma pequena faca."],
                        "Pacote de Explorador": ["Valor do pacote: 10 po",
                                                 "Inclui uma mochila, um saco de dormir, um kit de refeição, "
                                                 "uma caixa de fogo, 10 tochas, 10 dias de rações e um cantil."
                                                 " O kit também tem 15 metros de corda de cânhamo amarrada ao "
                                                 "lado dele."],
                        "Pacote de Sacerdote": ["Valor do pacote: 19 po",
                                                "Inclui uma mochila, um cobertor, 10 velas, uma caixa de fogo, "
                                                "uma caixa de esmolas, 2 blocos de incenso, um incensário, "
                                                "vestes, 2 dias de rações e um cantil."]}

    def __set_pacote__(self, pacote, attb):
        self.pacotes[pacote] = attb

    def __get_pacote__(self, pacote):
        return self.pacotes[pacote]
