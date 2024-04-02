from mensagens.mensagens import mensagem_normal


def forçar_parada(device):
    
    # Surf
    mensagem_normal('> Forçando parada dos aplicativos.')
    device.app_stop('com.surfshark.vpnclient.android')
    
    # Fast Vpn Freedom
    device.app_stop('easyvpn.free.vpn.unblock.proxy')
    
    # Vpn Unlimited Proxy
    device.app_stop('com.free.vpn.super.hotspot.open')
    
    # Varias Contas
    device.app_stop('com.excelliance.multiaccounts')
    