import os
from time import sleep

import uiautomator2 as u2

from _2nr.acessar_conta_2nr import acessar_conta_2nr
from _2nr.criar_numero import criando_numero
from _2nr.deletar_conta import deletar_conta
from atx import configurando_atx
from clonadores._2accounts import configurar_2_accounts
from clonadores.aplicativo_paralelo import configurar_aplicativo_paralelo
from clonadores.varias_contas import configurar_varias_contas
from configuracoes_usuario import configuracao
from instagram.criando_conta_instagram import iniciando_criacao_instagram
from mensagens.mensagens import mensagem_atencao
from utils.gerar_dados_perfil import gerar_dados_perfil
from utils.gerar_senha_perfil import gerar_senha_perfil
from vpn.avg_vpn.avg_vpn import avg_vpn_conect
from vpn.fast_vpn_freedom.fast_vpn_freedom import fast_vpn_freedom
from vpn.super_vpn_unlimited_proxy.vpn_unlimited_proxy import \
    vpn_unlimited_proxy
from vpn.surfsharke.surfshake import conectar_surfshake
from vpn.trocar_ip import trocar_ip


def main():
    # Configurações de usuário
    porta, definir_vpn, quantidade_contas_por_numero, velocidade_bot, genero, clonador = configuracao()
    os.system("adb devices")
    sleep(1)

    # configurando_atx()

    device = u2.connect(f'127.0.0.1:{porta}')  # Conectar ao UiAutomator2

    mensagem_atencao(' Iniciando automação...')
    sleep(1)
    print('')

    if definir_vpn == '1':
        vpns = [conectar_surfshake]
    elif definir_vpn == '2':
        vpns = [fast_vpn_freedom]
    elif definir_vpn == '3':
        vpns = [vpn_unlimited_proxy]
    elif definir_vpn == '4':
        vpns = [avg_vpn_conect]
    elif definir_vpn == '5':
        vpns = [conectar_surfshake, fast_vpn_freedom,
                vpn_unlimited_proxy, avg_vpn_conect]

    # Função para conectar na VPN
    trocar_ip(device, vpns, velocidade_bot=velocidade_bot)

    def acessar_conta():
        # Apagando conta 2nr e logando via gmail
        quantidade_tentativas = 0
        res = acessar_conta_2nr(
            device=device, velocidade_bot=velocidade_bot)
        if not res:
            while quantidade_tentativas < 4:
                trocar_ip(device=device, vpns=vpns,
                          velocidade_bot=velocidade_bot)
                res = acessar_conta_2nr(
                    device=device, velocidade_bot=velocidade_bot)
                if res:
                    break
                quantidade_tentativas += 1

    acessar_conta()

    while True:

        # Criando numero 2nr
        numero = criando_numero(device=device, velocidade_bot=velocidade_bot)
        if not numero:
            trocar_ip(device=device, vpns=vpns, velocidade_bot=velocidade_bot)
            continue
        # Se o limite de numeros criados for excedido
        if numero == 1:
            deletar_conta(device=device, velocidade_bot=velocidade_bot)
            acessar_conta()
            continue
        # Se existir tela de login
        if numero == 2:
            acessar_conta()
            continue

        for x in range(int(quantidade_contas_por_numero)):

            # Senha
            senha = gerar_senha_perfil()

            # nome
            nome, usuario = gerar_dados_perfil(genero=genero)

            # Configurando varias contas
            if clonador == '1':
                quantidade_tentativas = 0
                res = configurar_varias_contas(
                    device=device, velocidade_bot=velocidade_bot)
                if not res:
                    while quantidade_tentativas < 4:
                        trocar_ip(device=device, vpns=vpns,
                                  velocidade_bot=velocidade_bot)
                        res = configurar_varias_contas(
                            device=device, velocidade_bot=velocidade_bot)
                        if res:
                            break
                        quantidade_tentativas += 1

            if clonador == '2':
                quantidade_tentativas = 0
                res = configurar_2_accounts(
                    device=device, velocidade_bot=velocidade_bot)
                if not res:
                    while quantidade_tentativas < 4:
                        trocar_ip(device=device, vpns=vpns,
                                  velocidade_bot=velocidade_bot)
                        res = configurar_2_accounts(
                            device=device, velocidade_bot=velocidade_bot)
                        if res:
                            break
                        quantidade_tentativas += 1

            if clonador == '3':
                quantidade_tentativas = 0
                res = configurar_aplicativo_paralelo(
                    device=device, velocidade_bot=velocidade_bot)
                if not res:
                    while quantidade_tentativas < 4:
                        trocar_ip(device=device, vpns=vpns,
                                  velocidade_bot=velocidade_bot)
                        res = configurar_aplicativo_paralelo(
                            device=device, velocidade_bot=velocidade_bot)
                        if res:
                            break
                        quantidade_tentativas += 1

            # Iniciando criação
            res = iniciando_criacao_instagram(
                device=device, numero=numero, senha=senha, nome=nome, usuario=usuario, velocidade_bot=velocidade_bot)
            if not res:
                trocar_ip(device=device, vpns=vpns,
                          velocidade_bot=velocidade_bot)
                continue
            # Se o código não chegou, saia do lop for
            if res == 1:
                break
            # Se a conta foi suspensa, troca vpn e continua
            if res == 2:
                trocar_ip(device=device, vpns=vpns,
                          velocidade_bot=velocidade_bot)
                continue
            # Se criou, continua o lop
            if res == 3:
                continue
            # Se deu erro no numero, troca o ip e limpa dados do clonador.
            if res == 4:
                trocar_ip(device=device, vpns=vpns,
                          velocidade_bot=velocidade_bot)
                if clonador == '1':
                    res1 = configurar_varias_contas(
                        device=device, velocidade_bot=velocidade_bot)
                if clonador == '2':
                    res1 = configurar_2_accounts(
                        device=device, velocidade_bot=velocidade_bot)
                if clonador == '3':
                    res1 = configurar_aplicativo_paralelo(
                        device=device, velocidade_bot=velocidade_bot)

                res2 = iniciando_criacao_instagram(
                    device=device, numero=numero, senha=senha, nome=nome, usuario=usuario,
                    velocidade_bot=velocidade_bot)
                if not res1 or res2 == 4:
                    break
        else:
            continue  # Continua o lop while