import random


def gerar_dados_perfil():
        
    arquivo = open('./nomes/masculinas.txt', 'r', encoding="utf8")
    nomes = []

    for linha in arquivo:
        nome = linha.split('\n')[0]
        nomes.append(nome)

    nome1 = nomes[random.randint(1, len(nomes))]
    nome2 = nomes[random.randint(1, len(nomes))]
    nome3 = nomes[random.randint(1, len(nomes))]
    
    num = random.randint(1, 99)

    nome = nome1 + ' ' + nome2 + ' ' + nome3
    usuario = nome1.lower() + nome2.lower() + str(num) + nome3.lower()
    
    return nome, usuario