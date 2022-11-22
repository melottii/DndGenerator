from app.resources.equipamentos.armas import Armas
from app.resources.equipamentos.armaduras import Armaduras
from app.resources.equipamentos.equipamentos import Equipamentos

import random


class ItemPrototipo:
    def __init__(self):
        self.armas = Armas()
        self.armaduras = Armaduras()
        self.equipamentos = Equipamentos()

    def get_arma_marcial(self, nome):
        arma_dict = self.armas.__get_corpo_a_corpo_marcial__(nome)
        arma_obj = self.armas.__clone_arma__(arma_dict)
        return arma_obj

    def get_random_arma_marcial(self):
        arma = random.choice(self.armas.__get_corpo_a_corpo_marcial_list__())
        arma_obj = self.get_arma_marcial(arma)
        return arma_obj

    def get_arma_corpo_a_corpo_simples(self, nome):
        arma_dict = self.armas.__get_corpo_a_corpo_simples__(nome)
        arma_obj = self.armas.__clone_arma__(arma_dict)
        return arma_obj

    def get_random_arma_corpo_a_corpo_simples(self):
        arma = random.choice(self.armas.__get_corpo_a_corpo_simples_list__())
        arma_obj = self.get_arma_corpo_a_corpo_simples(arma)
        return arma_obj

    def get_arma_distancia_simples(self, nome):
        arma_dict = self.armas.__get_distancia_simples__(nome)
        arma_obj = self.armas.__clone_arma__(arma_dict)
        return arma_obj

    def get_random_arma_distancia_simples(self):
        arma = random.choice(self.armas.__get_distancia_simples_list__())
        arma_obj = self.get_arma_distancia_simples(arma)
        return arma_obj

    def get_arma_distancia_marcial(self, nome):
        arma_dict = self.armas.__get_distancia_marcial__(nome)
        arma_obj = self.armas.__clone_arma__(arma_dict)
        return arma_obj

    def get_random_arma_distancia_marcial(self):
        arma = random.choice(self.armas.__get_distancia_marcial_list__())
        arma_obj = self.get_arma_distancia_marcial(arma)
        return arma_obj

    def get_armadura_leve(self, nome):
        armadura_dict = self.armaduras.__get_leve__(nome)
        armadura_obj = self.armaduras.__clone_armadura__(armadura_dict)
        return armadura_obj

    def get_random_armadura_leve(self):
        armadura = random.choice(self.armaduras.__get_leve_list__())
        armadura_obj = self.get_armadura_leve(armadura)
        return armadura_obj

    def get_armadura_media(self, nome):
        armadura_dict = self.armaduras.__get_media__(nome)
        armadura_obj = self.armaduras.__clone_armadura__(armadura_dict)
        return armadura_obj

    def get_random_armadura_media(self):
        armadura = random.choice(self.armaduras.__get_media_list__())
        armadura_obj = self.get_armadura_media(armadura)
        return armadura_obj

    def get_armadura_pesada(self, nome):
        armadura_dict = self.armaduras.__get_pesada__(nome)
        armadura_obj = self.armaduras.__clone_armadura__(armadura_dict)
        return armadura_obj

    def get_random_armadura_pesada(self):
        armadura = random.choice(self.armaduras.__get_pesada_list__())
        armadura_obj = self.get_armadura_pesada(armadura)
        return armadura_obj

    def get_escudo(self, nome):
        armadura_dict = self.armaduras.__get_escudo__(nome)
        armadura_obj = self.armaduras.__clone_armadura__(armadura_dict)
        return armadura_obj

    def get_random_escudo(self):
        armadura = random.choice(self.armaduras.__get_escudo_list__())
        armadura_obj = self.get_escudo(armadura)
        return armadura_obj

    def get_pacote(self, nome):
        pacote_dict = self.equipamentos.__get_pacote__(nome)
        pacote_obj = self.equipamentos.__clone_pacote__(pacote_dict)
        return pacote_obj

    def get_random_pacote(self):
        pacote = random.choice(self.equipamentos.__get_pacote_list__())
        pacote_obj = self.get_escudo(pacote)
        return pacote_obj

    def get_equipamento(self, nome, quant):
        equip_dict = self.equipamentos.__get_equipamento__(nome)
        equip_obj = self.equipamentos.__clone_equipamento__(equip_dict, quant)
        return equip_obj

    def add_equipamentos_pacote(self, pacote, personagem):
        pacote.__set_config__(personagem)
