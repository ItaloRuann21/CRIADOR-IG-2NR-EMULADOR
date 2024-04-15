import random


def gerar_dados_perfil():
    arquivo = open('./nomes/masculinas.txt', 'r', encoding="utf8")
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

    num = random.randint(1, 99)

    nome = nome1 + ' ' + nome2 + ' ' + nome3
    usuario = nome1.lower() + nome2.lower() + str(num) + nome3.lower()

    return nome, usuario
