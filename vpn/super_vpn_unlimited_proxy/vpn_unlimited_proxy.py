from random import choice
from time import sleep

from Images.ManipularImagens import Imagem
from mensagens.mensagens import mensagem_normal


def paises_vpn_unlimited():

    arquivo = open('./vpn/super_vpn_unlimited_proxy/paises.txt',
                   'r', encoding='utf8')

    leia_arquivo = arquivo.readlines()

    pais = choice(leia_arquivo).strip()

    return pais


def vpn_unlimited_proxy(device):
    try:
        # Limpar dados
        mensagem_normal('> Limpando dados da Super VPN Unlimited Proxy')
        device.app_clear('com.free.vpn.super.hotspot.open')

        # Abrir VPN
        mensagem_normal('> Iniciando a Super VPN Unlimited Proxy')
        device.app_start('com.free.vpn.super.hotspot.open', use_monkey=True)

        # ACCEPT AND CONTINUE
        resposta = device(text='ACCEPT AND CONTINUE').exists(timeout=30)
        if resposta:
            device(text='ACCEPT AND CONTINUE').click()
        else:
            return False

        # Continuar com anúncios
        resposta = device(text='Continuar com anúncios').exists(timeout=30)
        if resposta:
            device(text='Continuar com anúncios').click()
        else:
            return False

        # Se aparecer anuncio na vpn (para uso em vps)
        mensagem_normal('> Escolhendo um país aleatório.')
        for x in range(30):

            # Se aparecer o anuncio, clica
            if device(text='Consentir').exists:
                device(text='Consentir').click()
                break

            # Ou se aparecer Localização rápida
            if device(text='Localização mais rápida').exists:
                device(text='Localização mais rápida').click()
                break

            # Ou se aparecer Alterar Servidor
            if device(text='Alterar servidor').exists:
                device(text='Alterar servidor').click()
                break

            sleep(1)

        # Escolher um servidor aleatório
        pais = paises_vpn_unlimited()
        mensagem_normal('> País escolhido: ' + pais)

        # Verificando se existe o pais para clicar
        for x in range(30):

            # Se existe o pais na tela, clica
            sleep(2)
            if device(text=pais).exists:
                device(text=pais).click()
                break

            # Se não existe, faz um swipe
            device.swipe(0.482, 0.887, 0.469, 0.353, 0.3)

            sleep(1)

        # Verificar se conectou com sucesso
        resposta = device(text='Conectado com sucesso').exists(timeout=10)
        if resposta:
            mensagem_normal('> VPN conectada.')
            device.press('home')

        return True
    except Exception as erro:
        print(erro)
        return False
