from random import choice


def pais_aleatorio():

    arquivo = open('./vpn/surfsharke/paises.txt', 'r', encoding='utf8')

    paises = arquivo.readlines()

    paises = choice(paises).strip()

    return paises
