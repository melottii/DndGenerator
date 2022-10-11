from builders.Classe import Classe


class Draconato(Classe):
    def __init__(self):
        super().__init__()
        self.name = "DRACONATO"

    def get_name(self):
        return "RAÇA: " + self.name
