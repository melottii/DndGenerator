class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __get_nome__(self):
        return self.nome
    
    def __set_nome__(self, nome):
        self.nome = nome

    def __get_email__(self):
        return self.email
    
    def __set_email__(self, email):
        self.email = email

    def __get_senha__(self):
        return self.senha

    def __set_senha__(self, senha):
        self.senha = senha
