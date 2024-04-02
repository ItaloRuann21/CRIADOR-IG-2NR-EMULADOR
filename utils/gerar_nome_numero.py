import string
from random import shuffle


def nome_do_numero():
    # Letras maiúsculas e minúsculas
    letras = string.ascii_letters

    senha = []

    # Adicionando letras maiúsculas e minúsculas
    for letra in letras:
        senha.append(letra)

    # Embaralhando a lista de caracteres
    shuffle(senha)

    # Juntando os caracteres em uma string
    nome_numero = ''.join(senha[:15])

    return nome_numero
