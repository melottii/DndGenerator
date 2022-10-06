from builders.FabricaPersonagem import PersonaInterface
from builders.Usuario import Usuario


class DndGenerator:
    def __init__(self):
        self.user = Usuario("Matheus", "matheus.melotti@gmail.com")
        self.character = PersonaInterface("Ladino")

    def printa_usuario(self):
        print(self.user.nome, self.user.email)

    def printa_personagem(self):
        print(self.character.person_class)


if __name__ == "__main__":
    first_person = DndGenerator()
    # first_person.printaPersonagem([first_person.user.nome, first_person.user.email])
    first_person.printa_usuario()
    first_person.printa_personagem()
