from app.builders.BuilderPersonagem import BuilderPersonagem
from app.builders.Usuario import Usuario


class DndGenerator:
    def __init__(self):
        self.user = Usuario("Matheus", "matheus.melotti@gmail.com")
        self.character = BuilderPersonagem()

    def define_escolhas(self):
        chosen_name = input("Nome do personagem: ")
        print("\nRaças cadastradas:")
        rc = {"1": "Anão da Colina",
              "2": "Anao da Montanha",
              "3": "Halfling Pés Leves",
              "4": "Halfling Robusto"}
        for a in rc:
            print(f"{a} - {rc[a]}")
        chosen_race = input("Número da Raça escolhida: ")
        if chosen_race not in rc:
            chosen_race = ""
        else:
            chosen_race = rc[chosen_race]

        cl = {"1": "Bárbaro",
              "2": "Bruxo",
              "3": "Ladino"}
        print("\nClasses Cadastradas:")
        for a in cl:
            print(f"{a} - {cl[a]}")
        chosen_class = input("Número da Classe escolhida: ")
        if chosen_class not in cl:
            chosen_class = ""
        else:
            chosen_class = cl[chosen_class]

        ant = {"1": "Acólito",
               "2": "Artesão de Guilda",
               "3": "Charlatão"}
        print("\nAntecedentes Cadastrados:")
        for a in ant:
            print(f"{a} - {ant[a]}")
        chosen_background = input("Número do Antecedente escolhido: ")
        if chosen_background not in ant:
            chosen_background = ""
        else:
            chosen_background = ant[chosen_background]
        print()
        return chosen_name, chosen_race, chosen_class, chosen_background

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
    chosen = first_person.define_escolhas()
    first_person.character = first_person.character.director(chosen[0], chosen[1], chosen[2], chosen[3])
    first_person.printa_personagem()
