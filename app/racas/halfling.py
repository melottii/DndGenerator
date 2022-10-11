from builders.Classe import Classe


class Halfling(Classe):
    def __init__(self):
        super().__init__()
        self.name = "HALFLING"

    def get_name(self):
        return "RAÇA: " + self.name
