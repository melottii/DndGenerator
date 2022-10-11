from builders.Classe import Classe


class MeioElfo(Classe):
    def __init__(self):
        super().__init__()
        self.name = "MEIO-ELFO"

    def get_name(self):
        return "RAÇA: " + self.name
