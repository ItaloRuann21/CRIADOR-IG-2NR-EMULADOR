from os import system
from random import choice
from time import sleep

import uiautomator2 as u2

from _2nr.acessar_conta_2nr import acessar_conta_2nr
from _2nr.criar_numero import criando_numero
from clonador.varias_contas import configurar_varias_contas
from configuracoes_usuario import configuracao
from instagram.criando_conta_instagram import iniciando_criacao_instagram
from mensagens.mensagens import (mensagem_atencao, mensagem_carregamento,
                                 mensagem_normal)
from utils.gerar_dados_perfil import gerar_dados_perfil
from utils.gerar_senha_perfil import gerar_senha_perfil
from utils.parando_aplicativos import forçar_parada
from vpn.escolher_vpn_aleatoria import escolher_vpn
from vpn.fast_vpn_freedom.fast_vpn_freedom import fast_vpn_freedom
from vpn.super_vpn_unlimited_proxy.vpn_unlimited_proxy import \
    vpn_unlimited_proxy
from vpn.surfsharke.surfshake import conectar_surfshake
from vpn.urban_vpn.urban_vpn import urban_vpn


def main():
    # Configurações de usuário
    porta = configuracao()

    device = u2.connect(f'127.0.0.1:{porta}')  # Conectar ao UiAutomator2

    mensagem_atencao('Iniciando automação...')
    sleep(1)
    mensagem_carregamento('Carregando...')
    print('')

    # Lista de VPNs disponíveis
    vpns = [conectar_surfshake, urban_vpn,
            fast_vpn_freedom, vpn_unlimited_proxy]

    # Lista para rastrear as VPNs já usadas
    vpns_usadas = []

    # Função para conectar na VPN
    def trocar_ip():
        # Forçar parada dos aplicativos
        forçar_parada(device=device)
        mensagem_normal('> Iniciando VPN aleatória.')
        vpn_escolhida = escolher_vpn(vpns_usadas, vpns)
        res = vpn_escolhida(device=device)
        if not res:
            return vpn_escolhida(device=device)

    # Chamar a função para trocar o IP
    trocar_ip()

    while True:

        # Senha
        senha = gerar_senha_perfil()

        # nome
        nome, usuario = gerar_dados_perfil()

        # Apagando conta 2nr
        quantidade_tentativas = 0
        res = acessar_conta_2nr(device=device)
        if not res:
            while quantidade_tentativas < 4:
                res = acessar_conta_2nr(device=device)
                if res:
                    break
                quantidade_tentativas += 1

        # Criando numero 2nr
        numero = criando_numero(device=device)
        if not numero:
            trocar_ip()
            continue

        for x in range(5):
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
            # Se o código não chegou, saia do loop for
            if res == 1000:
                break
        else:
            continue  # Continua o lop while


if __name__ == "__main__":
    main()
