from os import system
from random import choice
from time import sleep

import uiautomator2 as u2

from _2nr.apagar_conta_2nr import apagar_conta_2nr
from _2nr.criar_numero import criando_numero
from clonador.varias_contas import configurar_varias_contas
from configuracoes_usuario import configuracao
from instagram.criando_conta_instagram import iniciando_criacao_instagram
from mensagens.mensagens import (mensagem_atencao, mensagem_carregamento,
                                 mensagem_normal)
from utils.gerar_dados_perfil import gerar_dados_perfil
from utils.gerar_senha_perfil import gerar_senha_perfil
from utils.parando_aplicativos import forçar_parada
from vpn.fast_vpn_freedom.fast_vpn_freedom import fast_vpn_freedom
from vpn.super_vpn_unlimited_proxy.vpn_unlimited_proxy import \
    vpn_unlimited_proxy
from vpn.surfsharke.surfshake import conectar_surfshake
from vpn.urban_vpn.urban_vpn import urban_vpn


def main():
    # Configurações de usuário
    criacao, porta = configuracao()

    device = u2.connect(f'127.0.0.1:{porta}')  # Conectar ao UiAutomator2

    # Apagando o atx do aparelho
    system('adb shell pm uninstall com.github.uiautomator')

    mensagem_atencao('Iniciando automação...')
    sleep(1)
    mensagem_carregamento('Carregando...')
    print('')

    # Conectar na VPN
    def trocar_ip():
        # Forçando parada dos aplicativos
        forçar_parada(device=device)
        mensagem_normal('> Iniciando VPN aleatória.')
        vpns = [conectar_surfshake, fast_vpn_freedom,
                vpn_unlimited_proxy]
        vpn_escolhida = choice(vpns)
        res = vpn_escolhida(device=device)
        if not res:
            return vpn_escolhida(device=device)
    trocar_ip()

    for x in range(criacao):

        # Senha
        senha = gerar_senha_perfil()

        # nome
        nome, usuario = gerar_dados_perfil()

        # Apagando conta 2nr
        quantidade_tentativas = 0
        res = apagar_conta_2nr(device=device)
        if not res:
            while quantidade_tentativas < 4:
                mensagem_normal('> Tentando apagar a conta do 2nr novamente.')
                res = apagar_conta_2nr(device=device)
                if res:
                    break
                quantidade_tentativas += 1

        # Criando numero 2nr
        numero = criando_numero(device=device)
        if not numero:
            trocar_ip()
            continue

        # Configurando varias contas
        quantidade_tentativas = 0
        res = configurar_varias_contas(device=device)
        if not res:
            while quantidade_tentativas < 4:
                trocar_ip()
                res = configurar_varias_contas(device=device)
                if res:
                    break
                quantidade_tentativas += 1

        # Iniciando criação
        res = iniciando_criacao_instagram(
            device=device, numero=numero, senha=senha, nome=nome, usuario=usuario)
        if not res:
            trocar_ip()
            continue


if __name__ == "__main__":
    main()
