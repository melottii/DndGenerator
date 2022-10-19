from builders.FabricaPersonagem import PersonaInterface
from builders.Usuario import Usuario


class DndGenerator:
    def __init__(self):
        self.user = Usuario("Matheus", "matheus.melotti@gmail.com")
        self.character = PersonaInterface()

    def printa_usuario(self):
        print(self.user.nome)
        print(self.user.email)

    def printa_personagem(self):
        print(self.character.race.get_name())
        print(self.character.person_class.get_name())
        print(self.character.trend)
        print(self.character.money)
        print(self.character.dices["rolls"])
        print(self.character.dices["modifiers"])
        print(self.character.background_format["name"])
        print(self.character.background_format["type"])
        print(self.character.background_format["personality_trait"][0])
        print(self.character.background_format["personality_trait"][1])
        print(self.character.background_format["ideal"])
        print(self.character.background_format["flaw"])
        print(self.character.background_format["bond"])


if __name__ == "__main__":
    first_person = DndGenerator()
    first_person.character.director("Durat Diablo", "Anão", "Ladino", "CHARLATÃO")
    first_person.printa_personagem()
