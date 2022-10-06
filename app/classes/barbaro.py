from builders.Classe import Classe


class Barbaro(Classe):
    def __init__(self):
        super().__init__()
        self.name = "Barbaro"

    def get_name(self):
        return "CLASSE: " + self.name
