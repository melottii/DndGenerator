from app.builders.Classe import Classe


class Humano(Classe):
    def __init__(self):
        super().__init__()
        self.name = "HUMANO"

    def get_name(self):
        return "RAÇA: " + self.name
