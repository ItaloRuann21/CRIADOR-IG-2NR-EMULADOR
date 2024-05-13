

import shutil

from mensagens.mensagens import mensagem_atencao, mensagem_sucesso


def configuracao():

    print('')
    mensagem_atencao(' Digite a porta do emulador:')
    User_porta = input('> ')
    print('')
    porta = str(User_porta)
    mensagem_atencao(' Escolha o clonador:')
    clonador = input(
        '1- Varias Contas\n2- 2accounts\n3- Aplicativo Paralelo\n> ')
    print('')

    mensagem_atencao(' Escolha a VPN padrão:')
    definir_vpn = input(
        '1- SurfSharke\n2- Fast VPN Freedom\n3- Super VPN Unlimited Proxy\n4- AVG VPN\n5- Criação com VPN aleatória\n> ')
    print('')

    mensagem_atencao(' Criar quantas contas com mesmo número?')
    quantidade_contas_por_numero = input('> ')
    print('')
    mensagem_atencao(' Gênero dos perfis:')
    genero = input('1- Masculino\n2- Feminina\n> ')
    print('')

    mensagem_atencao(' Defina em segundos a velocidade do bot:')
    velocidade_bot = int(input('> '))
    print('')

    mensagem_atencao(' Defina qual opção você deseja:')
    _2nr = input('1- Logar no 2NR via Gmail\n2- Criação de conta 2nr\n> ')

    return porta, definir_vpn, quantidade_contas_por_numero, velocidade_bot, genero, _2nr, clonador
