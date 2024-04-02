


def configuracao():
    User_porta = input('Digite a porta do emulador\n> ')
    porta = str(User_porta)
    
    
    criacao = int(input('Criar quantas contas?\n> '))
    
    
    definir_vpn = int(input('Escolha a vpn:\n1 - Surfshake\n2 - Fast Vpn Freedom\n3 - Vpn Unlimited\n> '))
    
    
    return criacao, definir_vpn, porta
