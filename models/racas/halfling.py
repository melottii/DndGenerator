from models.Raca import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__()
        self.name = "Halfling"
        self.description = """
Os pequeninos halflings sobrevivem em um mundo cheio de criaturas maiores ao evitar serem notados, ou evitando o combate direto. Com uns 90 centímetros de altura, elesparecem inofensivos e assim conseguiram sobreviver por séculos às sombras dos impérios e à margem de guerras e conflitos políticos. Eles normalmente são robustos, pesando entre 20 kg e 22,5 kg. 
A pele dos halflings varia do bronzeado ao pálido com um tom corado, e seu cabelo é geralmente castanho ou castanho claro e ondulado. Eles têm olhos castanhos ou amendoados. Halflings do sexo masculino muitas vezes ostentam costeletas longas, mas barbas são raras entre eles e bigodes são quase inexistentes. Eles gostam de usar roupas simples, confortáveis e práticas, preferindo as cores claras. 
A praticidade dos halflings se estende para além de suas roupas. Eles se preocupam com as necessidades básicas e os prazeres simples, e não são inclinados à ostentação. Mesmo o mais rico dos halflings mantém seus tesouros trancados em um porão, em vez de expostos à vista de todos. Eles possuem um talento especial para encontrar a solução mais simples para um problema e têm pouca paciência para indecisões.
"""
        self.restrictions = []
        self.skills = [
            "Aumento no Valor de Habilidade. Seu valor de Destreza aumenta em 2. ",
            "Idade. Um halfling atinge a idade adulta aos 20 anos e pode chegar a 150 anos. ",
            "Tendência. A maioria dos halflings é leal e boa. Via de regra, eles possuem um bom coração e são amáveis, odeiam ver o sofrimento dos outros e não toleram a opressão. Eles também são muito ordeiros e tradicionais, fortemente apegados à sua comunidade e ao conforto de suas antigas tradições.",
            "Tamanho. Halflings medem cerca de 0,90 metro de altura e pesam aproximadamente 20 kg. Seu tamanho é Pequeno.",
            "Deslocamento. Seu deslocamento base de caminhada é 7,5 metros. ",
            "Sortudo. Quando você obtiver um 1 natural em uma jogada de ataque, teste de habilidade ou teste de resistência, você pode jogar de novo o dado e deve utilizar o novo resultado.",
            "Bravura. Você tem vantagem em testes de resistência contra ficar amedrontado. ",
            "Agilidade Halfling. Você pode mover-se através do espaço de qualquer criatura que for de um tamanho maior que o seu. ",
            "Idiomas. Você pode falar, ler e escrever Comum e Halfling. A linguagem Halfling não é secreta, mas os halflings são relutantes em compartilhá-la com os outros. Eles escrevem muito pouco, por isso eles não possuem uma literatura rica. No entanto, sua tradição oral é muito forte. Quase todos os halflings falam o idioma Comum para conversar com as pessoas das terras que habitam, ou através das quais eles estejam viajando. "
        ]
        self.magic = {}
        self.stats = {
            "strength": 0,
            "dexterity": 2,
            "constituition": 0,
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