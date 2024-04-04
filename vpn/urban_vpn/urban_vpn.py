
from random import choice
from time import sleep

from mensagens.mensagens import mensagem_erro, mensagem_normal


def paises_urban():
    arquivo = open('./vpn/urban_vpnpaises_urban.txt', 'r', encoding='utf8')
    ler_arquivos = arquivo.readlines()
    paises = choice(ler_arquivos).strip()
    return paises


def urban_vpn(device):
    try:

        # Limpar daods urban
        mensagem_normal('> Limpando dados da Urban VPN')
        device.app_clear('com.urbanvpn.android')

        # Abrir urban vpn
        mensagem_normal('> Conectando na Urban VPN')
        device.app_start('com.urbanvpn.android', use_monkey=True)

        # Choose Free
        if device(text='Choose Free').exists(timeout=30):
            device(text='Choose Free').click()
        sleep(2)

        # ACCEPT
        if device(text='ACCEPT').exists(timeout=30):
            device(text='ACCEPT').click()
        sleep(2)

        # Agree & Continue
        if device(text='Skip').exists(timeout=30):
            device(text='Skip').click()
        sleep(2)

        # Pesquisar pais
        paises = paises_urban()
        mensagem_normal('> País escolhido da urban vpn: ' + paises)
        if device(resourceId='com.urbanvpn.android:id/searchView').exists(timeout=30):
            device(resourceId='com.urbanvpn.android:id/searchView').click()
            device(resourceId='com.urbanvpn.android:id/searchView').set_text(paises)
        sleep(2)

        # Clicar no país
        if device(resourceId='com.urbanvpn.android:id/suggestion_name').exists(timeout=30):
            device(resourceId='com.urbanvpn.android:id/suggestion_name').click()

            # Se aparecer a mensagem para confirmar vpn, clica em OK
            if device(text='Solicitação de conexão').exists():
                device(text='OK').click()
        sleep(2)

        # Se a vpnc chegar na contagem de 5 segundos, então conectou
        if device(text='00 : 00 : 05').exists(timeout=7):
            return 'VPN Conectada!'

        return True
    except:
        mensagem_erro('> Não foi possível conectar na Urban VPN.')
        return False
