from app.builders.BuilderPersonagem import BuilderPersonagem
from interface.sessao import *

class DndGenerator:
    def __init__(self):
        self.user = login("vinicius@gmail.com", "123")
        self.character = BuilderPersonagem()

    def printa_usuario(self):
        print(self.user.nome)
        print(self.user.email)

    def printa_personagem(self):
        print(self.character.name)
        print(self.character.race.name)
        print(self.character.person_class.name)
        print(self.character.trend)
        print(self.character.money)
        self.printa_equipamentos()
        print(self.character.dices["rolls"])
        print(self.character.dices["modifiers"])
        print(self.character.background.background_format["name"])
        print(self.character.background.background_format["type"])
        print(self.character.background.background_format["personality_trait"][0])
        print(self.character.background.background_format["personality_trait"][1])
        print(self.character.background.background_format["ideal"])
        print(self.character.background.background_format["flaw"])
        print(self.character.background.background_format["bond"])
        print("Truques: ", list(self.character.magic[0].keys()))
        print("Magias: ", list(self.character.magic[1].keys()))
    
    def printa_equipamentos(self):
        for tipo in self.character.equip:
            print("\n" + tipo.upper() + ":")
            for equipamento in self.character.equip[tipo]:
                print(equipamento.nome, "x", equipamento.quantidade)



if __name__ == "__main__":
    first_person = DndGenerator()
    first_person.character = first_person.character.director("SPAM CAXOTA",
                                    "",
                                    "",
                                    "")
    print("Usuário: ", first_person.user.__get_nome__())
    first_person.printa_personagem()