from builders.Classe import Classe


class Tiefling(Classe):
    def __init__(self):
        super().__init__()
        self.name = "TIEFLING"

    def get_name(self):
        return "RAÇA: " + self.name
