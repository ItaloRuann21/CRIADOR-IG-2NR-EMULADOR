import time


def tempo_execucao(version_bot):
    while True:
        # Capturando o tempo atual
        tempo_atual = time.localtime()

        # Formatando o tempo para o formato desejado
        tempo_formatado = time.strftime(
            f"{version_bot} [%H:%M:%S]", tempo_atual)

        # Retornando o tempo formatado
        yield tempo_formatado
