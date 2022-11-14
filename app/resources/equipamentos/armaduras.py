from app.builders.Armadura import Armadura

class Armaduras:
    def __init__(self):
        self.leve = {
            "Acolchoada": {
                "preco": 5,
                "moeda": "po",
                "ca": 1,
                "furtividade": "",
                "peso": 4
            },
            "Couro": {
                "preco": 10,
                "moeda": "po",
                "ca": 1,
                "furtividade": "",
                "peso": 5
            },
            "Couro Batido": {
                "preco": 45,
                "moeda": "po",
                "ca": 2,
                "furtividade": "",
                "peso": 6.5
            }
        }

        self.media = {
            "Gibão de Peles": {
                "preco": 10,
                "moeda": "po",
                "ca": 2,
                "furtividade": "",
                "peso": 6
            },
            "Camisão de Malha": {
                "preco": 50,
                "moeda": "po",
                "ca": 3,
                "furtividade": "",
                "peso": 10
            }, 
            "Brunea": {
                "preco": 50,
                "moeda": "po",
                "ca": 4,
                "furtividade": "Desvantagem",
                "peso": 22.5
            }, 
            "Peitoral de Aço": {
                "preco": 400,
                "moeda": "po",
                "ca": 4,
                "furtividade": "",
                "peso": 10
            }, 
            "Meia-Armudura": {
                "preco": 750,
                "moeda": "po",
                "ca": 5,
                "furtividade": "Desvantagem",
                "peso": 20
            }
        }

        self.pesada = {
            "Cota de Anéis": {
                "preco": 30,
                "moeda": "po",
                "ca": 2,
                "furtividade": "Desvantagem",
                "peso": 20
            },
            "Cota de Malha": {
                "preco": 75,
                "moeda": "po",
                "ca": 6,
                "furtividade": "Desvantagem",
                "peso": 22.5
            },
            "Cota de Talas": {
                "preco": 200,
                "moeda": "po",
                "ca": 7,
                "furtividade": "Desvantagem",
                "peso": 30
            },
            "Armadura de Placas": {
                "preco": 150,
                "moeda": "po",
                "ca": 8,
                "furtividade": "Desvantagem",
                "peso": 32.5
            }
        }

        self.escudo = {
            "Escudo": {
                "preco": 10,
                "moeda": "po",
                "ca": 2,
                "furtividade": "",
                "peso": 3
            }
        }
    
    def __get_leve__(self, param):
        return {param: self.leve[param]}
    
    def __get_media__(self, param):
        return {param: self.media[param]}

    def __get_pesada__(self, param):
        return {param: self.pesada[param]}

    def __get_escudo__(self, param):
        return {param: self.escudo[param]}

    def __get_leve_list__(self):
        return [i for i in self.leve.keys()]

    def __set_leve_simples__(self, param, attb):
        self.leve[param] = attb

    def __get_media_list__(self):
        return [i for i in self.media.keys()]

    def __set_media_simples__(self, param, attb):
        self.media[param] = attb

    def __get_pesada_list__(self):
        return [i for i in self.pesada.keys()]

    def __set_pesada_simples__(self, param, attb):
        self.pesada[param] = attb
    
    def __get_escudo_list__(self):
        return [i for i in self.escudo.keys()]

    def __set_escudo__(self, param, attb):
        self.escudo[param] = attb

    def __clone_armadura__(self, armadura_dict):
        for armadura in armadura_dict:
            armadura_obj = Armadura(
                armadura,
                armadura_dict[armadura]["preco"],
                armadura_dict[armadura]["moeda"],
                armadura_dict[armadura]["peso"],
                1,
                armadura_dict[armadura]["ca"],
                armadura_dict[armadura]["furtividade"]
            )
            return armadura_obj