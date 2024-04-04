from random import choice


def paises_fast_vpn():

    arquivo = open('./vpn/fast_vpn_freedom/paises_fast_vpn.txt',
                   'r', encoding='utf8')

    leia_arquivo = arquivo.readlines()

    pais = choice(leia_arquivo).strip()

    return pais
