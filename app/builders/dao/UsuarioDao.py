from dotenv import load_dotenv

import pymongo
import os
import sys

load_dotenv()

db_url = os.getenv("MONGO_URL")

client = pymongo.MongoClient(db_url)

db = client.dndgenerator

users = db.users


class UsuarioDao:
    @staticmethod
    def getUsuario(email):
        try:
            user = users.find_one({"email": email})
            return user
        except Exception as e:
            sys.exit(f"ERRO AO LER OS DADOS DO BANCO: {e}")

    @staticmethod
    def getAllUsuarios():
        try:
            users_list = []
            cursor = users.find({})
            for document in cursor:
                users_list.append(document)
            return users_list
        except Exception as e:
            sys.exit(f"ERRO AO LER OS DADOS DO BANCO: {e}")

    @staticmethod
    def deleteUsuario(email):
        try:
            query = {"email": email}
            users.delete_one(query)
            return True
        except Exception as e:
            sys.exit(f"ERRO AO ALTERAR O REGISTRO NA BASE DE DADOS: {e}")

    @staticmethod
    def updateUsuario(usuario):
        try:
            user = {
                "nome": usuario.__get_nome__(),
                "email": usuario.__get_email__(),
                "senha": usuario.__get_senha__()
            }
            query = {"email": user["email"]}

            users.update_one(query, {"$set": user})
            return True
        except Exception as e:
            sys.exit(f"ERRO AO ALTERAR O REGISTRO NA BASE DE DADOS: {e}")

    def createUsuario(self, usuario):
        try:
            criou = False
            existe = self.getUsuario(usuario.__get_email__())
            if existe is None:
                user = {
                    "nome": usuario.__get_nome__(),
                    "email": usuario.__get_email__(),
                    "senha": usuario.__get_senha__()
                }
                users.insert_one(user)
                criou = True
            return criou
        except Exception as e:
            sys.exit(f"ERRO AO INCLUIR O USUÁRIO NO BANCO DE DADOS: {e}")
