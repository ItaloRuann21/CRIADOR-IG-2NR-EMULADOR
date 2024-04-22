import random


def gerar_dados_perfil(genero):

    if genero == '1':
        arquivo = open('./nomes/masculinas.txt', 'r', encoding="utf8")
    else:
        arquivo = open('./nomes/femininas.txt', 'r', encoding="utf8")

    nomes = []

    for linha in arquivo:
        # Use strip() para remover espaços em branco extras, incluindo a quebra de linha
        nome = linha.strip()
        nomes.append(nome)

    if len(nomes) < 3:
        raise ValueError("Não há nomes suficientes para gerar um perfil")

    # Ajuste dos índices para começar do 0
    nome1 = nomes[random.randint(0, len(nomes) - 1)]
    nome2 = nomes[random.randint(0, len(nomes) - 1)]
    nome3 = nomes[random.randint(0, len(nomes) - 1)]

    num = random.randint(1, 999)

    nome = nome1 + ' ' + nome2 + ' ' + nome3
    usuario = nome1.lower() + nome2.lower() + nome3.lower() + str(num)

    return nome, usuario
