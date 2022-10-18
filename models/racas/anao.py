from models.Raca import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__()
        self.nome = "Anão"
        self.descricao = """
Audazes e resistentes, os anões são conhecidos como hábeis guerreiros, mineradores e trabalhadores em pedra e metal. Embora tenham menos de 1,50 metro de altura, os anões são tão largos e compactos que podem pesar tanto quanto um humano 60 centímetros mais alto. Sua coragem e resistência compete facilmente com qualquer povo mais alto. A pele dos anões varia do marrom escuro a um matiz mais pálido, tingido de vermelho, mas os tons mais comuns são o castanho claro ou bronzeado, como certos tons terrosos. O cabelo é longo, mas de estilo simples, geralmente negro, cinzento ou castanho, embora anões mais pálidos frequentemente possuem cabelos ruivos. Anões machos valorizam altamente suas barbas e preparam-nas com cuidado.
"""
        self.restricoes = []
        self.habilidadesUnicas = [
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
        self.magias = []
        self.forca = 0
        self.destreza = 0
        self.constituicao = 2
        self.sabedoria = 0
        self.inteligencia = 0
        self.carisma = 0

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_descricao(self):
        return self.descricao
    
    def set_desricao(self, descricao):
        self.descricao = descricao

    def get_restricoes(self):
        return self.restricoes
    
    def set_restricoes(self, restricoes):
        self.restricoes = restricoes
    
    def get_habilidadesUnicas(self):
        return self.habilidadesUnicas
    
    def set_habilidadesUnicas(self, habilidadesUnicas):
        self.habilidadesUnicas = habilidadesUnicas

    def add_habilidade(self, habilidade):
        self.habilidadesUnicas.append(habilidade)

    def get_magias(self):
        return self.magias
    
    def set_magias(self, magias):
        self.magias = magias

    def get_forca(self):
        return self.forca
    
    def set_forca(self, forca):
        self.forca = forca

    def get_destreza(self):
        return self.destreza
    
    def set_destreza(self, destreza):
        self.destreza = destreza
    
    def get_constituicao(self):
        return self.constituicao
    
    def set_constituicao(self, constituicao):
        self.constituicao = constituicao
    
    def get_sabedoria(self):
        return self.sabedoria
    
    def set_sabedoria(self, sabedoria):
        self.sabedoria = sabedoria
    
    def get_inteligencia(self):
        return self.inteligencia
    
    def set_inteligencia(self, inteligencia):
        self.inteligencia = inteligencia

    def get_carisma(self):
        return self.carisma
    
    def set_carisma(self, carisma):
        self.carisma = carisma
    
    def add_atributo(self, atributo, quantidade):
        atributos = {
            1: self.set_forca(self.forca+quantidade),
            2: self.set_destreza(self.destreza+quantidade),
            3: self.set_constituicao(self.contituicao+quantidade),
            4: self.set_sabedoria(self.sabedoria+quantidade),
            5: self.set_inteligencia(self.inteligencia+quantidade),
            6: self.set_carisma(self.carisma+quantidade),
        }
        atributos[atributo]
