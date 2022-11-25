from app.builders.Usuario import Usuario
from app.builders.dao.UsuarioDao import UsuarioDao

usuarioDao = UsuarioDao()


def login():
    email = str(input("Email: "))
    senha = str(input("Senha: "))
    usuario = usuarioDao.getUsuario(email)
    if usuario is not None:
        if usuario["senha"] == senha:
            user = Usuario(
                usuario["nome"],
                usuario["email"],
                usuario["senha"]
            )
            return user
    return False


def cadastro(nome, email, senha):
    usuario = usuarioDao.getUsuario(email)
    if usuario is None:
        user = Usuario(nome, email, senha)
        usuarioDao.createUsuario(user)
        return user
    return False
