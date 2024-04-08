from random import choice


# Função para escolher uma VPN aleatória, garantindo que não seja repetida
def escolher_vpn(vpns_usadas, vpns):
    # Se todas as VPNs já foram usadas, redefinir a lista de VPNs usadas
    if len(vpns_usadas) == len(vpns):
        vpns_usadas.clear()
    # Escolher uma VPN aleatória que ainda não foi usada
    vpn_escolhida = choice(
        [vpn for vpn in vpns if vpn not in vpns_usadas])
    vpns_usadas.append(vpn_escolhida)
    return vpn_escolhida