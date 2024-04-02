from mensagens.mensagens import mensagem_normal
from vpn.paises_fast_vpn_freedom import paises_fast_vpn


def vpn_unlimited_proxy(device):
    try:
        # Limpar dados
        mensagem_normal('> Limpando dados da VPN Unlimited Proxy')
        device.app_clear('com.free.vpn.super.hotspot.open')
        
        # Abrir VPN
        device.app_start('com.free.vpn.super.hotspot.open', use_monkey=True)
        
        # ACCEPT AND CONTINUE
        try:
            device(resourceId='com.free.vpn.super.hotspot.open:id/btnAgree').wait(30)
            device(resourceId='com.free.vpn.super.hotspot.open:id/btnAgree').click()
        except:
            return False
        
        # Continuar com anúncios
        try:
            device(text='Continuar com anúncios').wait(30)
            device(text='Continuar com anúncios').click()
        except:
            return False
        
        # Localização mais rápida
        try:
            device(resourceId='com.free.vpn.super.hotspot.open:id/tv_fastest_server').wait(60)
            device(resourceId='com.free.vpn.super.hotspot.open:id/tv_fastest_server').click()
        except:
            return False
        
        # Escolher pais aleatorio da america do norte ou sul
        pais = paises_fast_vpn()
        mensagem_normal('> País escolhido: ' + pais)
        
        while True:
            '''Nesse While, o IF verifica se o pais existe, se existe, clica. ELSE > Rola até encontrar o pais certo'''
            if device(text=pais).exists:
                device(text=pais).click()
                break
            else:
                device.swipe(0.501, 0.9, 0.485, 0.335)
            
        # Solicitando Conexão
        if device(resourceId='android:id/alertTitle').exists:
            device(text='OK').click()
        
        # Verificar se conectou com sucesso
        if device(text='Conectado com sucesso').wait(30):
            device.press('home')
            return True
        else:
            return False
        
    except Exception as erro:
        print(erro)
        return False