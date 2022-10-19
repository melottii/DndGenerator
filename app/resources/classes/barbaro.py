from app.builders.Classe import Classe


class Barbaro(Classe):
    def __init__(self):
        super().__init__()
        self.name = "BARBARO"

    def get_name(self):
        return "CLASSE: " + self.name
