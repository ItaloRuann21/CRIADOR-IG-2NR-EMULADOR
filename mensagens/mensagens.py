import sys
from time import sleep

from colorama import Back, Fore, Style, init

from tempo_terminal.tempo import tempo_execucao

# Inicializa o colorama
tempo = tempo_execucao(Fore.CYAN + 'Creator IG v7.0.8' + Style.RESET_ALL)
init()


def mensagem_normal(mensagem):
    print(next(tempo) + mensagem)


def mensagem_sucesso(mensagem):
    print(next(tempo) + Fore.GREEN + mensagem + Style.RESET_ALL)


def mensagem_erro(mensagem):
    print(next(tempo) + Fore.RED + mensagem + Style.RESET_ALL)


def mensagem_desativada(mensagem):
    print(next(tempo) + Fore.MAGENTA + mensagem + Style.RESET_ALL)


def mensagem_info(mensagem):
    print(next(tempo) + Fore.LIGHTBLUE_EX + mensagem + Style.RESET_ALL)


def mensagem_atencao(mensagem):
    print(next(tempo) + Fore.YELLOW + mensagem + Style.RESET_ALL)
