from app.builders.Classe import Classe


class Ladino(Classe):
    def __init__(self):
        super().__init__()
        self.name = "LADINO"

    def get_name(self):
        return "CLASSE: " + self.name