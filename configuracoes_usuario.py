


def configuracao():
    User_porta = input('Digite a porta do emulador\n> ')
    porta = str(User_porta)
    
    
    criacao = int(input('Criar quantas contas?\n> '))
    
    
    definir_vpn = int(input('Escolha a vpn:\n1-Surfshake 2-Fast Vpn Freedom 3-Vpn Unlimited 4-Urban VPN\n> '))
    
    
    return criacao, definir_vpn, porta
