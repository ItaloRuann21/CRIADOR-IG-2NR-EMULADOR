from time import sleep

from mensagens.mensagens import (mensagem_atencao, mensagem_erro,
                                 mensagem_normal)

from .paises_fast_vpn_freedom import paises_fast_vpn


def fast_vpn_freedom(device, velocidade_bot):
    try:
        mensagem_atencao('> Iniciando a Fast Vpn Freedom.')

        # limpar dados fast
        sleep(velocidade_bot)
        mensagem_normal('> Limpando dados da Fast VPN')
        device.app_clear('easyvpn.free.vpn.unblock.proxy')
        sleep(velocidade_bot)

        # Abrir fast
        device.app_start('easyvpn.free.vpn.unblock.proxy', use_monkey=True)
        sleep(velocidade_bot)

        # ACCEPT AND CONTINUE
        resposta = device(text='ACCEPT AND CONTINUE').exists(timeout=30)
        if resposta:
            device(text='ACCEPT AND CONTINUE').click()
        else:
            mensagem_erro('> Não clicou em ACCEPT AND CONTINUE')
            return False
        sleep(velocidade_bot)

        mensagem_normal('> Escolhendo um país aleatório.')
        # clicar em Localização mais rápida
        for x in range(30):

            # Se aparecer Alterar servidor, clica
            if device(text='Alterar servidor').exists:
                device(text='Alterar servidor').click()
                break

            # Se aparecer Localização mais rápida, clica
            if device(text='Localização mais rápida').exists:
                device(text='Localização mais rápida').click()
                break

            sleep(1)
        sleep(velocidade_bot)

        # Esperar seletor pra saber que carregou todos os paiss
        resposta = device(text='Fastest Location').exists(timeout=30)
        if not resposta:
            return False
        sleep(velocidade_bot)

        # Escolher um servidor aleatório
        pais = paises_fast_vpn()
        mensagem_normal('> País escolhido: ' + pais)

        # Verificando se existe o pais para clicar
        for x in range(60):

            # Se existe o pais na tela, clica
            sleep(2)
            if device(text=pais).exists:
                device(text=pais).click()
                break

            # Se não existe, faz um swipe
            device.swipe(0.472, 0.907, 0.514, 0.431, 0.04)

            sleep(1)
        sleep(velocidade_bot)

        # Verificar se conectou com sucesso
        resposta = device(text='Conectado com sucesso').exists(timeout=10)
        if resposta:
            mensagem_normal('> VPN conectada.')
            device.press('home')
            sleep(velocidade_bot)
            return True

    except Exception as erro:
        print(erro)
        return False
