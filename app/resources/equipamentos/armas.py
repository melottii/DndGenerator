from app.builders.prototipo.Arma import Arma

class Armas:
    def __init__(self):
        self.corpo_a_corpo_simples = {
            "Adaga": {"preco": 2, "moeda": "po","dano": "1d4", "peso": "0.5 kg",
                        "propriedades": ["Acuidade", "Leve", "Arremesso (distância 6/18)"]},

                "Azagaia": {"preco": 5, "moeda": "pp","dano": "1d6", "peso": "1 kg",
                            "propriedades": ["Perfurante", "Arremesso (distância 9/36)"]},

                "Bordão": {"preco": 2, "moeda": "pp", "dano": "1d6", "peso": "2 kg",
                            "propriedades": ["Concussão", "Versátil (1d8)"]},

                "Clava Grande": {"preco": 2, "moeda": "pp","dano": "1d8", "peso": "5 kg",
                                "propriedades": ["Concussão", "Pesada", "Duas mãos"]},

                "Foice curta": {"preco": 1, "moeda": "po", "dano": "1d4", "peso": "1   kg",
                                "propriedades": ["Cortante", "Leve"]},

                "Lança": {"preco": 1, "moeda": "po","dano": "1d6", "peso": "1.5 kg",
                        "propriedades": ["Perfurante", "Arremesso (6/18)", "Versátil (1d8)"]},

                "Maça": {"preco": 5, "moeda": "po", "dano": "1d6", "peso": "2 kg",
                        "propriedades": ["Concussão"]},

                "Machadinha": {"preco": 5, "moeda": "po", "dano": "1d6", "peso": " 1kg",
                                "propriedades": ["Leve Arremesso"]},
                                
                "Martelo Leve": {"preco": 2, "moeda": "po", "dano": "1d4", "peso": "1 kg",
                                "propriedades": ["Concussão", "Leve", "Arremesso (distância 6/18)"]},

                "Porrete": {"preco": 1, "moeda": "pp", "dano": "1d4", "peso": "1 kg",
                            "propriedades": ["Concussão", "Leve"]}
                }

        self.distancia_simples = {
            "Arco Curto": {"preco": 25, "moeda": "po", "dano": "1d6", "peso": "1 kg",
                "propriedades": ["Perfurante", "Duas mãos","Munição (distância 24/96)"]},

            "Besta Leve": {"preco": 25, "moeda": "po", "dano": "1d8", "peso": "2.5 kg",
                "propriedades": ["Perfurante", "Recarga", "Duas mãos","Munição (distância 24/96)"]},

            "Dardo": {"preco": 5, "moeda": "pc", "dano": "1d4", "peso": "0.1 kg",
                "propriedades": ["Perfurante", "Acuidade", "Arremesso (distância 6/18)"]},

            "Funda": {"preco": 25, "moeda": "po", "dano": "1d8", "peso": "2.5 kg",
                "propriedades": ["Concussão", "Munição (distância 9/36)"]}
        }

        self.corpo_a_corpo_marcial = {
            "Alabarda": {"preco": 20, "moeda": "po", "dano": "1d10", "peso": "3 kg",
                        "propriedades": ["Cortante", "Leve", "Arremesso (distância 6/18)"]},

            "Cimitarra": {"preco": 25, "moeda": "po", "dano": "1d6", "peso": "1.5 kg",
                        "propriedades": ["Cortante", "Arremesso (distância 9/36)"]},

            "Chicote": {"preco": 2, "moeda": "po", "dano": "1d4", "peso": "1.5 kg",
                        "propriedades": ["Cortante, ""Versátil (1d8)"]},

            "Espada Curta": {"preco": 10, "moeda": "po", "dano": "1d6", "peso": "1 kg",
                            "propriedades": ["Perfurante", "Pesada", "Duas mãos"]},

            "Espada Grande": {"preco": 50, "moeda": "po", "dano": "2d6", "peso": "3 kg",
                            "propriedades": ["Cortante", "Leve"]},

            "Espada Longa": {"preco": 15, "moeda": "po", "dano": "1d8", "peso": "1.5 kg",
                            "propriedades": ["Cortante", "Arremesso (6/18)",
                                            "Versátil (1d8)"]},

            "Glaive": {"preco": 20, "moeda": "po", "dano": "1d10", "peso": "3 kg",
                        "propriedades": ["Cortante"]},

            "Lança de Montaria": {"preco": 10, "moeda": "po", "dano": "1d12", "peso": " 1kg",
                                "propriedades": ["Perfurante", "Leve Arremesso"]},

            "Lança Longa": {"preco": 5, "moeda": "po", "dano": "1d10", "peso": "3 kg",
                            "propriedades": ["Perfurante", "Leve","Arremesso (distância 6/18)"]},

            "Maça Estrela": {"preco": 15, "moeda": "po", "dano": "1d8", "peso": "4 kg",
                            "propriedades": ["Perfurante", "Leve"]},

            "Machado Grande": {"preco": 30, "moeda": "po", "dano": "1d12", "peso": "2 kg",
                                "propriedades": ["Cortante", "Leve"]},

            "Machado de Batalha": {"preco": 10, "moeda": "po", "dano": "1d8", "peso": "3.5 kg",
                                    "propriedades": ["Cortante", "Leve"]},

            "Malho": {"preco": 10, "moeda": "po", "dano": "2d6", "peso": "5 kg",
                    "propriedades": ["Concussão", "Leve"]},

            "Mangual": {"preco": 10, "moeda": "po", "dano": "1d8", "peso": "1 kg",
                        "propriedades": ["Concussão", "Leve"]},

            "Martelo de Guerra": {"preco": 10, "moeda": "po", "dano": "1d8", "peso": "1 kg",
                                "propriedades": ["Concussão", "Leve"]},

            "Picareta de Guerra": {"preco": 5, "moeda": "po", "dano": "1d8", "peso": "1 kg",
                                    "propriedades": ["Perfurante", "Leve"]},

            "Rapieira": {"preco": 25, "moeda": "po", "dano": "1d8", "peso": "1 kg",
                        "propriedades": ["Perfurante", "Acuidade"]},

            "Tridente": {"preco": 5 , "moeda": "po", "dano": "1d6", "peso": "2 kg",
                        "propriedades": ["Perfurante", "Arremesso (6/18)", "Versátil (1d8)"]}
        }

        self.distancia_marcial = {
            "Arco Longo": {"preco": 50, "moeda": "po", "dano": "1d8", "peso": "1 kg",
                    "propriedades": ["Perfurante", "Duas mãos", "Pesada",
                                    "Munição (distância 45/180)"]},

            "Besta de Mão": {"preco": 75, "moeda": "po", "dano": "1d6", "peso": "1.5 kg",
                "propriedades": ["Perfurante", "Recarga", "Leve",
                                "Munição (distância 9/36)"]},

            "Besta Pesada": {"preco": 50, "moeda": "po", "dano": "1d10", "peso": "4.5 kg",
                "propriedades": ["Perfurante", "Acuidade","Arremesso (distância 30/120)",
                "Pesada", "Recarga","Duas Mãos"]},

            "Rede": {"preco": 1, "moeda": "po", "dano": "-", "peso": "1.5 kg",
                "propriedades": ["Especial", "Munição (distância 1.5/4.5)"]},

            "Zarabatana": {"preco": 10,"moeda": "po", "dano": "1", "peso": "0.5 kg",
                "propriedades": ["Perfurante", "Munição (distância 7.5/30)",
                                "Recarga"]}
        }

    def __get_corpo_a_corpo_simples__(self, param):
        return {param: self.corpo_a_corpo_simples[param]}

    def __get_corpo_a_corpo_marcial__(self, param):
        return {param: self.corpo_a_corpo_marcial[param]}

    def __get_distancia_simples__(self, param):
        return {param: self.distancia_simples[param]}

    def __get_distancia_marcial__(self, param):
        {param: self.distancia_marcial[param]}

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

    def __clone_arma__(self, arma_dict):
        for arma in arma_dict:
            arma_obj = Arma(
                arma,
                arma_dict[arma]["preco"],
                arma_dict[arma]["moeda"],
                arma_dict[arma]["peso"],
                1,
                arma_dict[arma]["dano"],
                arma_dict[arma]["propriedades"]
            )
            return arma_obj
