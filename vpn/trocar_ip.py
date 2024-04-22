from mensagens.mensagens import mensagem_normal
from utils.parando_aplicativos import forçar_parada
from vpn.escolher_vpn_aleatoria import escolher_vpn

# Lista para rastrear as VPNs já usadas
vpns_usadas = []


def trocar_ip(device, vpns, velocidade_bot):
    # Forçar parada dos aplicativos
    forçar_parada(device=device)
    vpn_escolhida = escolher_vpn(vpns_usadas, vpns)
    res = vpn_escolhida(device=device, velocidade_bot=velocidade_bot)
    if not res:
        return vpn_escolhida(device=device, velocidade_bot=velocidade_bot)
