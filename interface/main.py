from builders.FabricaPersonagem import PersonaInterface
from builders.Usuario import Usuario


class DndGenerator:
    def __init__(self):
        self.user = Usuario("Matheus", "matheus.melotti@gmail.com")
        self.character = PersonaInterface("Durat Diablo",
                                          "Elfo",
                                          "Ladino",
                                          [15, 0, 0, 0, 0, 0])

    def printa_usuario(self):
        print(self.user.nome)
        print(self.user.email)

    def printa_personagem(self):
        print(self.character.race.get_name())
        print(self.character.person_class.get_name())
        print(self.character.dices["rolls"])
        print(self.character.dices["modifiers"])


if __name__ == "__main__":
    first_person = DndGenerator()
    first_person.printa_usuario()
    first_person.printa_personagem()
