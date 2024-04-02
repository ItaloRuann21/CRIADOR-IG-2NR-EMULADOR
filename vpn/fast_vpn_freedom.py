from time import sleep

from mensagens.mensagens import mensagem_normal
from vpn.paises_fast_vpn_freedom import paises_fast_vpn


def fast_vpn_freedom(device):
    try:
        
        # limpar dados fast
        mensagem_normal('> Limpando dados da Fast VPN')
        device.app_clear('easyvpn.free.vpn.unblock.proxy')
        
        # Abrir fast
        device.app_start('easyvpn.free.vpn.unblock.proxy', use_monkey=True)
        
        # AGREE
        device(resourceId='easyvpn.free.vpn.unblock.proxy:id/btnAgree').wait(30)
        device(resourceId='easyvpn.free.vpn.unblock.proxy:id/btnAgree').click()
        
        # Localização mais rápida
        device(resourceId='easyvpn.free.vpn.unblock.proxy:id/tv_fastest_server').wait(60)
        device(resourceId='easyvpn.free.vpn.unblock.proxy:id/tv_fastest_server').click()
        
        # Escolher pais aleatorio da america do norte ou sul
        pais = paises_fast_vpn()
        mensagem_normal('> País escolhido: ' + pais)
        
        contador = 0
        while contador < 30:
            '''Nesse While, o IF verifica se o pais existe, se existe, clica. ELSE > Rola até encontrar o pais certo'''
            sleep(1)
            if device(text=pais).exists:
                device(text=pais).click()
                break
            else:
                device.swipe(0.501, 0.9, 0.485, 0.335)
                contador += 1
        
        # Solicitando Conexão
        if device(resourceId='android:id/alertTitle').exists:
            device(text='OK').click()
        
        # Verificar se conectou com sucesso
        if device(text='Conectado com sucesso').wait(30):
            mensagem_normal('> VPN conectada.')
            device.press('home')
            return True

    except Exception as erro:
        print(erro)
        return False