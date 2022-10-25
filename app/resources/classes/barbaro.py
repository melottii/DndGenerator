from app.builders.Classe import Classe


class Barbaro(Classe):
    def __init__(self):
        super().__init__()
        self.name = "BÁRBARO"

    def get_name(self):
        return f"CLASSE: {self.name}"
