from builders.Classe import Classe


class MeioOrc(Classe):
    def __init__(self):
        super().__init__()
        self.name = "MEIO-ORC"

    def get_name(self):
        return "RAÇA: " + self.name
