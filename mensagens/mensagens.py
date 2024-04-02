
import sys
from time import sleep

from termcolor import colored


def mensagem_normal(mensagem):
    print(mensagem)

def mensagem_sucesso(mensagem):
    print(colored(mensagem, 'green'))

def mensagem_carregamento(mensagem, duracao=1):
    carregamento = ['|', '/', '-', '\\']
    mensagem_sem_carregamento = f'{mensagem} '
    for _ in range(duracao * 10):
        for char in carregamento:
            sys.stdout.write('\r' + mensagem_sem_carregamento + char)
            sys.stdout.flush()
            sleep(0.1)

def mensagem_erro(mensagem):
    print(colored(mensagem, 'red'))
    
def mensagem_atencao(mensagem):
    print(colored(mensagem, 'yellow'))
    