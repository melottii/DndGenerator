class Armaduras:
    def __init__(self):
        self.leve = {
            "nome": ["Acolchoada", "Couro", "Couro Batido"],
            "preco": [5, 10, 45],
            "moeda": "po",
            "ca": [1, 1, 2],
            "furtividade": ["", "", ""],
            "peso": [4, 5, 6.5]
        }

        self.media = {
            "nome": ["Gibão de Peles", "Camisão de Malha", "Brunea", "Peitoral de Aço", "Meia-Armudura"],
            "preco": [10, 50, 50, 400, 750],
            "moeda": "po",
            "ca": [2, 3, 4, 4, 5],
            "furtividade": ["", "", "Desvantagem", "", "Desvantagem"],
            "peso": [6, 10, 22.5, 10, 20]
        }

        self.pesada = {
            "nome": ["Cota de Anéis", "Cota de Malha", "Cota de Talas", "Armadura de Placas"],
            "preco": [30, 75, 200, 150],
            "moeda": "po",
            "ca": [2, 6, 7, 8],  # Forca minima para CA CA6 >= F13, CA7 >= F15,
            "furtividade": ["Desvantagem", "Desvantagem", "Desvantagem", "Desvantagem", "Desvantagem"],
            "peso": [20, 22.5, 30, 32.5]
        }

        self.escudo = {
            "nome": "Escudo",
            "preco": 10,
            "moeda": "po",
            "ca": +2,
            "furtividade": "",
            "peso": 3
        }
