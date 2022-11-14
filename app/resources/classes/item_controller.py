from app.resources.equipamentos.armas import Armas
from app.resources.equipamentos.armaduras import Armaduras
from app.resources.equipamentos.equipamentos import Equipamentos

import random

armas = Armas()
armaduras = Armaduras()
equipamentos = Equipamentos()

def get_arma_marcial(nome):
    arma_dict = armas.__get_corpo_a_corpo_marcial__(nome)
    arma_obj = armas.__clone_arma__(arma_dict)
    return arma_obj

def get_random_arma_marcial():
   arma = random.choice(armas.__get_corpo_a_corpo_marcial_list__())
   arma_obj = get_arma_marcial(arma)
   return arma_obj

def get_arma_corpo_a_corpo_simples(nome):
    arma_dict = armas.__get_corpo_a_corpo_simples__(nome)
    arma_obj = armas.__clone_arma__(arma_dict)
    return arma_obj

def get_random_arma_corpo_a_corpo_simples():
   arma = random.choice(armas.__get_corpo_a_corpo_simples_list__())
   arma_obj = get_arma_corpo_a_corpo_simples(arma)
   return arma_obj

def get_arma_distancia_simples(nome):
    arma_dict = armas.__get_distancia_simples__(nome)
    arma_obj = armas.__clone_arma__(arma_dict)
    return arma_obj

def get_random_arma_distancia_simples():
   arma = random.choice(armas.__get_distancia_simples_list__())
   arma_obj = get_arma_distancia_simples(arma)
   return arma_obj

def get_arma_distancia_marcial(nome):
    arma_dict = armas.__get_distancia_marcial__(nome)
    arma_obj = armas.__clone_arma__(arma_dict)
    return arma_obj

def get_random_arma_distancia_marcial():
   arma = random.choice(armas.__get_distancia_marcial_list__())
   arma_obj = get_arma_distancia_marcial(arma)
   return arma_obj

def get_armadura_leve(nome):
    armadura_dict = armaduras.__get_leve__(nome)
    armadura_obj = armaduras.__clone_armadura__(armadura_dict)
    return armadura_obj

def get_random_armadura_leve():
   armadura = random.choice(armaduras.__get_leve_list__())
   armadura_obj = get_armadura_leve(armadura)
   return armadura_obj

def get_armadura_media(nome):
    armadura_dict = armaduras.__get_media__(nome)
    armadura_obj = armaduras.__clone_armadura__(armadura_dict)
    return armadura_obj

def get_random_armadura_media():
   armadura = random.choice(armaduras.__get_media_list__())
   armadura_obj = get_armadura_media(armadura)
   return armadura_obj

def get_armadura_pesada(nome):
    armadura_dict = armaduras.__get_pesada__(nome)
    armadura_obj = armaduras.__clone_armadura__(armadura_dict)
    return armadura_obj

def get_random_armadura_pesada():
   armadura = random.choice(armaduras.__get_pesada_list__())
   armadura_obj = get_armadura_pesada(armadura)
   return armadura_obj

def get_escudo(nome):
    armadura_dict = armaduras.__get_escudo__(nome)
    armadura_obj = armaduras.__clone_armadura__(armadura_dict)
    return armadura_obj

def get_random_escudo():
   armadura = random.choice(armaduras.__get_escudo_list__())
   armadura_obj = get_escudo(armadura)
   return armadura_obj

def get_pacote(nome):
    pacote_dict = equipamentos.__get_pacote__(nome)
    pacote_obj = equipamentos.__clone_pacote__(pacote_dict)
    return pacote_obj

def get_random_pacote():
   pacote = random.choice(equipamentos.__get_pacote_list__())
   pacote_obj = get_escudo(pacote)
   return pacote_obj

def get_equipamento(nome, quant):
    equip_dict = equipamentos.__get_equipamento__(nome)
    equip_obj = equipamentos.__clone_equipamento__(equip_dict, quant)
    return equip_obj

def add_equipamentos_pacote(pacote, personagem):
    pacote.__set_config__(personagem)