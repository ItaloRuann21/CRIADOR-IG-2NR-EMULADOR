from random import choice

# Lista para rastrear os países já usados
paises_usados = []


def pais_aleatorio():
    global paises_usados  # Declarando que vamos usar a variável global dentro da função

    # Lista de países disponíveis
    paises_arquivo = open('./vpn/surfsharke/paises.txt', 'r', encoding='utf8')
    paises_disponiveis = paises_arquivo.readlines()

    # Se todos os países já foram usados, redefinir a lista de países usados
    if len(paises_usados) == len(paises_disponiveis):
        paises_usados.clear()

    # Escolher um país aleatório que ainda não foi usado
    paises_nao_usados = []
    for pais in paises_disponiveis:
        if pais.strip() not in paises_usados:
            paises_nao_usados.append(pais.strip())
    pais_escolhido = choice(paises_nao_usados)
    paises_usados.append(pais_escolhido.strip())

    return pais_escolhido.strip()
