from app.builders.Classe import Classe


class Bruxo(Classe):
    def __init__(self):
        super().__init__()
        self.name = "BRUXO"

    def get_name(self):
        return "CLASSE: " + self.name
