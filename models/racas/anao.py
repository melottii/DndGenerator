from models.Raca import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__()
        self.name = "Anão"
        self.description = """
Audazes e resistentes, os anões são conhecidos como hábeis guerreiros, mineradores e trabalhadores em pedra e metal. Embora tenham menos de 1,50 metro de altura, os anões são tão largos e compactos que podem pesar tanto quanto um humano 60 centímetros mais alto. Sua coragem e resistência compete facilmente com qualquer povo mais alto. A pele dos anões varia do marrom escuro a um matiz mais pálido, tingido de vermelho, mas os tons mais comuns são o castanho claro ou bronzeado, como certos tons terrosos. O cabelo é longo, mas de estilo simples, geralmente negro, cinzento ou castanho, embora anões mais pálidos frequentemente possuem cabelos ruivos. Anões machos valorizam altamente suas barbas e preparam-nas com cuidado.
"""
        self.restrictions = []
        self.skills = [
            "Aumento no Valor de Habilidade. Seu valor de Constituição aumenta em 2.",
            "Idade. Anões tornam-se maduros na mesma proporção que os humanos, mas são considerados jovens até atingirem a idade de 50 anos. Em média, eles vivem 350 anos.",
            "Tendência. A maioria dos anões é leal, pois acreditam firmemente nos benefícios de uma sociedade bem organizada. Eles tendem para o bem, com um forte senso de honestidade e uma crença de que todos merecem compartilhar os benefícios de uma ordem social justa.",
            "Tamanho. Anões estão entre 1,20 e 1,50 metro de altura e pesam cerca de 75 kg. Seu tamanho é Médio.",
            "Deslocamento. Seu deslocamento base de caminhada é de 7,5 metros. Seu deslocamento não é reduzido quando estiver usando armadura pesada.",
            "Visão no Escuro. Acostumado à vida subterrânea, você tem uma visão superior no escuro e na penumbra. Você enxerga na penumbra a até 18 metros como se fosse luz plena, e no escuro como se fosse na penumbra. Você não pode discernir cores no escuro, apenas tons de cinza.",
            "Resiliência Anã. Você possui vantagem em testes de resistência contra venenos e resistência contra dano de veneno.",
            "Treinamento Anão em Combate. Você tem proficiência com machados de batalha, machadinhas, martelos leves e martelos de guerra.",
            "Proficiência com Ferramentas. Você tem proficiência em uma ferramenta de artesão à sua escolha entre: ferramentas de ferreiro, suprimentos de cervejeiro ou ferramentas de pedreiro.",
            "Especialização em Rochas. Sempre que você realizar um teste de Inteligência (História) relacionado à origem de um trabalho em pedra, você é considerado proficiente na perícia História e adiciona o dobro do seu bônus de proficiência ao teste, ao invés do seu bônus de proficiência normal.",
            "Idiomas. Você pode falar, ler e escrever Comum e Anão. O idioma Anão é repleto de consoantes duras e sons guturais, e essa característica influencia, como um sotaque, qualquer outro idioma que o anão falar.",
            "Sub-raça. Existem duas sub-raças principais de anões nos mundos de D&D: anões da colina e anões da montanha. Você deve escolher uma dessas sub-raças. "
        ]
        self.magic = {}
        self.stats = {
            "strength": 0,
            "dexterity": 0,
            "constituition": 2,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
        }

    def __get_name__(self):
        return self.name
    
    def __set_name__(self, name):
        self.name = name

    def __get_description__(self):
        return self.description
    
    def __set_desricao__(self, description):
        self.description = description

    def __get_restrictions__(self):
        return self.restrictions
    
    def __set_restrictions__(self, restrictions):
        self.restrictions = restrictions
    
    def __get_skills__(self):
        return self.skills
    
    def __set_skills__(self, skills):
        self.skills = skills

    def __add_skill__(self, skill):
        self.skills.append(skill)

    def __get_magic__(self):
        return self.magic
    
    def __set_magic__(self, magic):
        self.magic = magic

    def __get_strength__(self):
        return self.stats["strength"]
    
    def __set_strength__(self, strength):
        self.stats["strength"] = strength

    def __get_dexterity__(self):
        return self.stats["dexterity"]
    
    def __set_dexterity__(self, dexterity):
        self.stats["dexterity"] = dexterity
    
    def __get_constituition__(self):
        return self.stats["constituition"]
    
    def __set_constituition__(self, constituition):
        self.self.stats["constituition"] = constituition
    
    def __get_wisdom__(self):
        return self.stats["wisdom"]
    
    def __set_wisdom__(self, wisdom):
        self.stats["wisdom"] = wisdom
    
    def __get_intelligence__(self):
        return self.stats["intelligence"]
    
    def __set_intelligence__(self, intelligence):
        return self.stats["intelligence"] = intelligence

    def __get_charisma__(self):
        return self.stats["charisma"]
    
    def __set_charisma__(self, charisma):
        self.stats["charisma"] = charisma
