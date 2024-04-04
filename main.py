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
from vpn.fast_vpn_freedom import fast_vpn_freedom
from vpn.surfshake import conectar_surfshake
from vpn.urban_vpn import urban_vpn
from vpn.vpn_unlimited_proxy import vpn_unlimited_proxy


def main():
    # Configurações de usuário
    criacao, definir_vpn, porta = configuracao()

    device = u2.connect(f'127.0.0.1:{porta}')  # Conectar ao UiAutomator2

    mensagem_atencao('Iniciando automação...')
    sleep(1)
    mensagem_carregamento('Carregando...')
    print('')

    # Forçando parada dos aplicativos
    forçar_parada(device=device)

    # Senha
    senha = gerar_senha_perfil()

    # nome
    nome, usuario = gerar_dados_perfil()

    # Conectar na VPN
    def trocar_ip():
        if definir_vpn == 1:
            res = conectar_surfshake(device=device)
            if not res:
                return conectar_surfshake(device=device)
        elif definir_vpn == 2:
            res = fast_vpn_freedom(device=device)
            if not res:
                return fast_vpn_freedom(device=device)
        elif definir_vpn == 3:
            res = vpn_unlimited_proxy(device=device)
            if not res:
                return vpn_unlimited_proxy(device=device)
        elif definir_vpn == 4:
            res = urban_vpn(device=device)
            if not res:
                return urban_vpn(device=device)
    trocar_ip()

    for x in range(criacao):

        # Apagando conta 2nr
        quantidade_tentativas = 0
        res = apagar_conta_2nr(device=device)
        if not res:
            while quantidade_tentativas < 4:
                trocar_ip()
                mensagem_normal('> Tentando novamente')
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
