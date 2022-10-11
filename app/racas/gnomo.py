from builders.Classe import Classe


class Gnomo(Classe):
    def __init__(self):
        super().__init__()
        self.name = "GNOMO"

    def get_name(self):
        return "RAÇA: " + self.name
