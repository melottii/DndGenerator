from builders.FabricaPersonagem import PersonaInterface
from builders.Usuario import Usuario


class DndGenerator:
    def __init__(self):
        self.user = Usuario("Matheus", "matheus.melotti@gmail.com")
        self.character = PersonaInterface("Durat Diablo",
                                          "Anão",
                                          "Ladino",
                                          "Artesao De Guilda")

    def printa_usuario(self):
        print(self.user.nome)
        print(self.user.email)

    def printa_personagem(self):
        print(self.character.race.get_name())
        print(self.character.person_class.get_name())
        print(self.character.trend)
        print(self.character.dices["rolls"])
        print(self.character.dices["modifiers"])
        print(self.character.antecedent.get_name(self.character))
        print(self.character.antecedent.get_type(self.character))
        print(self.character.antecedent.get_personality_trait(self.character))
        print(self.character.antecedent.get_ideal(self.character))
        print(self.character.antecedent.get_flaw(self.character))
        print(self.character.antecedent.get_bond(self.character))


if __name__ == "__main__":
    first_person = DndGenerator()
    first_person.printa_usuario()
    first_person.printa_personagem()
