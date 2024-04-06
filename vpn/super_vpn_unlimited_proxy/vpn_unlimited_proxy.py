from random import choice
from time import sleep

from Images.ManipularImagens import Imagem
from mensagens.mensagens import mensagem_normal


def vpn_unlimited_proxy(device):
    try:
        # Limpar dados
        mensagem_normal('> Limpando dados da VPN Unlimited Proxy')
        device.app_clear('com.free.vpn.super.hotspot.open')

        # Abrir VPN
        device.app_start('com.free.vpn.super.hotspot.open', use_monkey=True)

        # ACCEPT AND CONTINUE
        imagem = Imagem(device)
        try:
            imagem.clicar_na_imagem(
                './Images/super_vpn_unlimited/accept_and_continue.png')
        except:
            device(text='ACCEPT AND CONTINUE').click()

        # Continuar com anúncios
        imagem.clicar_na_imagem(
            './Images/super_vpn_unlimited/continuar_com_anuncio.png')

        # Se aparecer anuncio na vpn (para uso em vps)
        if imagem.esperar_imagem(
                './Images/super_vpn_unlimited/consentir.png'):
            mensagem_normal('> Anúncio existe na vps unlimited')
            imagem.clicar_na_imagem(
                './Images/super_vpn_unlimited/consentir.png')

        # Localização mais rápida
        imagem.clicar_na_imagem(
            './Images/super_vpn_unlimited/localizacao_mais_rapida.png')

        # Recarregar duas vezes a lista de paises
        imagem.clicar_na_imagem(
            './Images/super_vpn_unlimited/recarregar.png')
        imagem.clicar_na_imagem(
            './Images/super_vpn_unlimited/recarregar.png')
        sleep(2)

        # Clicando em lugares aleatorios
        device.click(0.058, 0.649)

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
