class Armas:
    def __init__(self):
        self.corpo_a_corpo_simples = {"Adaga": {"Preço": "2 po", "Dano": "1d4", "Peso": "0.5 kg",
                                                "Propriedades": ["Acuidade", "Leve", "Arremesso (distância 6/18)"]},
                                      "Azagaia": {"Preço": "5 pp", "Dano": "1d6", "Peso": "1 kg",
                                                  "Propriedades": ["Perfurante", "Arremesso (distância 9/36)"]},
                                      "Bordão": {"Preço": "2 pp", "Dano": "1d6", "Peso": "2 kg",
                                                 "Propriedades": ["Concussão, ""Versátil (1d8)"]},
                                      "Clava Grande": {"Preço": "2 pp", "Dano": "1d8", "Peso": "5 kg",
                                                       "Propriedades": ["Concussão", "Pesada", "Duas mãos"]},
                                      "Foice curta": {"Preço": "1 po", "Dano": "1d4", "Peso": "1   kg",
                                                      "Propriedades": ["Cortante", "Leve"]},
                                      "Lança": {"Preço": "1 po", "Dano": "1d6", "Peso": "1.5 kg",
                                                "Propriedades": ["Perfurante", "Arremesso (6/18)", "Versátil (1d8)"]},
                                      "Maça": {"Preço": "5 po", "Dano": "1d6", "Peso": "2 kg",
                                               "Propriedades": ["Concussão"]},
                                      "Machadinha": {"Preço": "5 po", "Dano": "1d6", "Peso": " 1kg",
                                                     "Propriedades": ["Leve Arremesso"]},
                                      "Martelo Leve": {"Preço": "2 po", "Dano": "1d4", "Peso": "1 kg",
                                                       "Propriedades": ["Concussão", "Leve",
                                                                        "Arremesso (distância 6/18)"]},
                                      "Porrete": {"Preço": "1 pp", "Dano": "1d4", "Peso": "1 kg",
                                                  "Propriedades": ["Concussão", "Leve"]}}

        self.distancia_simples = {"Arco Curto": {"Preço": "25 po", "Dano": "1d6", "Peso": "1 kg",
                                                 "Propriedades": ["Perfurante", "Duas mãos",
                                                                  "Munição (distância 24/96)"]},
                                  "Besta Leve": {"Preço": "25 po", "Dano": "1d8", "Peso": "2.5 kg",
                                                 "Propriedades": ["Perfurante", "Recarga", "Duas mãos",
                                                                  "Munição (distância 24/96)"]},
                                  "Dardo": {"Preço": "5 pc", "Dano": "1d4", "Peso": "0.1 kg",
                                            "Propriedades": ["Perfurante", "Acuidade", "Arremesso (distância 6/18)"]},
                                  "Funda": {"Preço": "25 po", "Dano": "1d8", "Peso": "2.5 kg",
                                            "Propriedades": ["Concussão", "Munição (distância 9/36)"]}}

        self.corpo_a_corpo_marcial = {"Alabarda": {"Preço": "20 po", "Dano": "1d10", "Peso": "3 kg",
                                                   "Propriedades": ["Cortante", "Leve", "Arremesso (distância 6/18)"]},
                                      "Cimitarra": {"Preço": "25 po", "Dano": "1d6", "Peso": "1.5 kg",
                                                    "Propriedades": ["Cortante", "Arremesso (distância 9/36)"]},
                                      "Chicote": {"Preço": "2 po", "Dano": "1d4", "Peso": "1.5 kg",
                                                  "Propriedades": ["Cortante, ""Versátil (1d8)"]},
                                      "Espada Curta": {"Preço": "10 po", "Dano": "1d6", "Peso": "1 kg",
                                                       "Propriedades": ["Perfurante", "Pesada", "Duas mãos"]},
                                      "Espada Grande": {"Preço": "50 po", "Dano": "2d6", "Peso": "3 kg",
                                                        "Propriedades": ["Cortante", "Leve"]},
                                      "Espada Longa": {"Preço": "15 po", "Dano": "1d8", "Peso": "1.5 kg",
                                                       "Propriedades": ["Cortante", "Arremesso (6/18)",
                                                                        "Versátil (1d8)"]},
                                      "Glaive": {"Preço": "20 po", "Dano": "1d10", "Peso": "3 kg",
                                                 "Propriedades": ["Cortante"]},
                                      "Lança de Montaria": {"Preço": "10 po", "Dano": "1d12", "Peso": " 1kg",
                                                            "Propriedades": ["Perfurante", "Leve Arremesso"]},
                                      "Lança Longa": {"Preço": "5 po", "Dano": "1d10", "Peso": "3 kg",
                                                      "Propriedades": ["Perfurante", "Leve",
                                                                       "Arremesso (distância 6/18)"]},
                                      "Maça Estrela": {"Preço": "15 po", "Dano": "1d8", "Peso": "4 kg",
                                                       "Propriedades": ["Perfurante", "Leve"]},
                                      "Machado Grande": {"Preço": "30 po", "Dano": "1d12", "Peso": "2 kg",
                                                         "Propriedades": ["Cortante", "Leve"]},
                                      "Machado de Batalha": {"Preço": "10 po", "Dano": "1d8", "Peso": "3.5 kg",
                                                             "Propriedades": ["Cortante", "Leve"]},
                                      "Malho": {"Preço": "10 po", "Dano": "2d6", "Peso": "5 kg",
                                                "Propriedades": ["Concussão", "Leve"]},
                                      "Mangual": {"Preço": "10 po", "Dano": "1d8", "Peso": "1 kg",
                                                  "Propriedades": ["Concussão", "Leve"]},
                                      "Martelo de Guerra": {"Preço": "10 po", "Dano": "1d8", "Peso": "1 kg",
                                                            "Propriedades": ["Concussão", "Leve"]},
                                      "Picareta de Guerra": {"Preço": "5 po", "Dano": "1d8", "Peso": "1 kg",
                                                             "Propriedades": ["Perfurante", "Leve"]},
                                      "Rapieira": {"Preço": "25 po", "Dano": "1d8", "Peso": "1 kg",
                                                   "Propriedades": ["Perfurante", "Acuidade"]},
                                      "Tridente": {"Preço": "5 po", "Dano": "1d6", "Peso": "2 kg",
                                                   "Propriedades": ["Perfurante", "Arremesso (6/18)",
                                                                    "Versátil (1d8)"]}}

        self.distancia_marcial = {"Arco Longo": {"Preço": "50 po", "Dano": "1d8", "Peso": "1 kg",
                                                 "Propriedades": ["Perfurante", "Duas mãos", "Pesada",
                                                                  "Munição (distância 45/180)"]},
                                  "Besta de Mão": {"Preço": "75 po", "Dano": "1d6", "Peso": "1.5 kg",
                                                   "Propriedades": ["Perfurante", "Recarga", "Leve",
                                                                    "Munição (distância 9/36)"]},
                                  "Besta Pesada": {"Preço": "50 po", "Dano": "1d10", "Peso": "4.5 kg",
                                                   "Propriedades": ["Perfurante", "Acuidade",
                                                                    "Arremesso (distância 30/120)", "Pesada", "Recarga",
                                                                    "Duas Mãos"]},
                                  "Rede": {"Preço": "1 po", "Dano": "-", "Peso": "1.5 kg",
                                           "Propriedades": ["Especial", "Munição (distância 1.5/4.5)"]},
                                  "Zarabatana": {"Preço": "10 po", "Dano": "1", "Peso": "0.5 kg",
                                                 "Propriedades": ["Perfurante", "Munição (distância 7.5/30)",
                                                                  "Recarga"]}}

    def __get_corpo_a_corpo_simples__(self, param):
        return self.corpo_a_corpo_simples[param]

    def __get_corpo_a_corpo_marcial__(self, param):
        return self.corpo_a_corpo_marcial[param]

    def __get_distancia_simples__(self, param):
        return self.distancia_simples[param]

    def __get_distancia_marcial__(self, param):
        return self.distancia_marcial[param]

    def __get_corpo_a_corpo_marcial_list__(self):
        return [i for i in self.corpo_a_corpo_marcial.keys()]

    def __get_corpo_a_corpo_simples_list__(self):
        return [i for i in self.corpo_a_corpo_simples.keys()]

    def __get_distancia_marcial_list__(self):
        return [i for i in self.distancia_marcial.keys()]

    def __get_distancia_simples_list__(self):
        return [i for i in self.distancia_simples.keys()]

    def __set_corpo_a_corpo_simples__(self, param, attb):
        self.corpo_a_corpo_simples[param] = attb

    def __set_corpo_a_corpo_marcial__(self, param, attb):
        self.corpo_a_corpo_marcial[param] = attb

    def __set_distancia_simples__(self, param, attb):
        self.distancia_simples[param] = attb

    def __set_distancia_marcial__(self, param, attb):
        self.distancia_marcial[param] = attb
