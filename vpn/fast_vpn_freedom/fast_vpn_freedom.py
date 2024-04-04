from time import sleep

from Images.ManipularImagens import Imagem
from mensagens.mensagens import mensagem_atencao, mensagem_normal


def fast_vpn_freedom(device):
    try:
        mensagem_atencao('> Iniciando a Fast Vpn Freedom.')

        # limpar dados fast
        mensagem_normal('> Limpando dados da Fast VPN')
        device.app_clear('easyvpn.free.vpn.unblock.proxy')

        # Abrir fast
        device.app_start('easyvpn.free.vpn.unblock.proxy', use_monkey=True)

        # AGREE
        imagem = Imagem(device)
        imagem.clicar_na_imagem(
            './Images/fast_vpn_freedom/accept_and_continue.png')

        # Localização mais rápida
        mensagem_normal('> Escolhendo um país aleatório.')
        if device(resourceId='easyvpn.free.vpn.unblock.proxy:id/tv_fastest_server').exists(timeout=10):
            device(
                resourceId='easyvpn.free.vpn.unblock.proxy:id/tv_fastest_server').click()

        # Esperar algum seletor da vpn aparecer
        if device(text='Fastest Location').exists(20):
            # Clicando no meio
            device.click(0.061, 0.649)

        # Solicitando Conexão
        if device(resourceId='android:id/alertTitle').exists(timeout=3):
            device(text='OK').click()

        # Verificar se conectou com sucesso
        if device(text='Conectado com sucesso').wait(30):
            mensagem_normal('> VPN conectada.')
            device.press('home')
            return True

    except Exception as erro:
        print(erro)
        return False
