import sys
from time import sleep

from colorama import Back, Fore, Style, init

# Inicializa o colorama
init()


def mensagem_normal(mensagem):
    print(mensagem)


def mensagem_sucesso(mensagem):
    print(Fore.GREEN + mensagem + Style.RESET_ALL)


def mensagem_carregamento(mensagem, duracao=1):
    carregamento = ['|', '/', '-', '\\']
    mensagem_sem_carregamento = f'{mensagem} '
    for _ in range(duracao * 10):
        for char in carregamento:
            sys.stdout.write('\r' + mensagem_sem_carregamento + char)
            sys.stdout.flush()
            sleep(0.1)


def mensagem_erro(mensagem):
    print(Fore.RED + mensagem + Style.RESET_ALL)


def mensagem_atencao(mensagem):
    print(Fore.YELLOW + mensagem + Style.RESET_ALL)
