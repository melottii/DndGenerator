from builders.Classe import Classe


class Elfo(Classe):
    def __init__(self):
        super().__init__()
        self.name = "ELFO"

    def get_name(self):
        return "RAÇA: " + self.name
