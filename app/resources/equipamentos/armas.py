class Armas:
    def __init__(self):
        self.corpo_a_corpo = {"nome": ["Adaga", "Lança", "Porrete", "Espada Curta", "Machado Grande"],
                              "preco": ["2", " 1", " 1", " 10", "30 "], "moeda": ["po", "po", "pp", "po", "po"],
                              "dado_dano": ["1d4", "1d6", "1d4", "1d6", "1d12"],
                              "tipo_dano": ["perfurante", "perfurante", "concussão", "perfurante", "cortante"],
                              "peso": [0.5, 1.6, 1, 1, 3.5],
                              "propriedade": [["Acuidade", "leve", "arremesso", "(distância 6/18)"],
                                              ["Arremesso", "(distância 6/18)", " versátil(1d8)"], ["leve"],
                                              ["Acuidade", "leve"], ["Pesada", "duas mãos"]]}

        self.distancia = {"nome": ["Arco Curto", "Arco Longo", ], "preco": ["25", "50"], "moeda": ["po", "po"],
                          "dado_dano": ["1d4", "1d8", ], "tipo_dano": ["perfurante", "perfurante"], "peso": [0.1, 1],
                          "propriedade": [["Munição", "(distância 24/96)", "duas mãos "],
                                          ["Munição", "(distância 45/180)", "pesada", " duas mãos"]]}
