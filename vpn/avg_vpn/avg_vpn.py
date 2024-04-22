from random import choice
from time import sleep

from mensagens.mensagens import mensagem_atencao, mensagem_normal

# Lista para rastrear os países já usados
paises_usados = []


def pais_aleatorio_avg():
    global paises_usados  # Declarando que vamos usar a variável global dentro da função

    # Lista de países disponíveis
    paises_arquivo = open('./vpn/avg_vpn/paises.txt', 'r', encoding='utf8')
    paises_disponiveis = paises_arquivo.readlines()

    # Se todos os países já foram usados, redefinir a lista de países usados
    if len(paises_usados) == len(paises_disponiveis):
        paises_usados.clear()

    # Escolher um país aleatório que ainda não foi usado
    paises_nao_usados = []
    for pais in paises_disponiveis:
        if pais.strip() not in paises_usados:
            paises_nao_usados.append(pais.strip())
    pais_escolhido = choice(paises_nao_usados)
    paises_usados.append(pais_escolhido.strip())

    return pais_escolhido.strip()


def avg_vpn_conect(device, velocidade_bot):
    try:

        # Escolhendo quais paises serão usados
        pais_escolhido = pais_aleatorio_avg()

        # Entrar avg
        sleep(velocidade_bot)
        mensagem_atencao(' Iniciando a AVG VPN')
        device.app_start('com.avg.android.vpn', use_monkey=True)
        sleep(velocidade_bot)

        # Se aparecer mensagem de avaliação de 5 estrelas
        if device(text='Você está recebendo uma experiência 5 estrelas?').exists(timeout=5):
            sleep(1)
            device.press('back')
        sleep(velocidade_bot)

        # Verificando se a vpn está conectada.
        resposta = device(
            resourceId='com.avg.android.vpn:id/on').exists(timeout=5)
        if resposta:
            device(resourceId='com.avg.android.vpn:id/on').click()
            mensagem_normal(' Desconectando VPN')
        sleep(velocidade_bot)

        # Clicar em Localização Ideal
        mensagem_normal(' Escolhendo um país aleatório.')
        resposta = device(
            resourceId='com.avg.android.vpn:id/location_arrow').exists(timeout=10)
        if resposta:
            device(resourceId='com.avg.android.vpn:id/location_arrow').click()
        else:
            return False
        sleep(velocidade_bot)

        mensagem_normal(' País escolhido: ' + pais_escolhido)
        # Verificando se existe o pais para clicar
        for x in range(60):

            # Se existe o pais na tela, clica
            sleep(2)
            if device(text=pais_escolhido).exists:
                device(text=pais_escolhido).click()
                break

            # Se não existe, faz um swipe
            device.swipe(0.472, 0.907, 0.514, 0.431, 0.2)

            sleep(1)
        sleep(velocidade_bot)

        # Se aparecer para solicitar a conexão, clica em OK
        for x in range(10):

            # Confirmar conexão
            if device(text='Solicitação de conexão').exists:
                device(text='OK').click()

            # Se aparecer ativar a conexão automatica
            if device(text='ATIVAR A CONEXÃO AUTOMÁTICA').exists:
                device.press('back')

            # Verificar se conectou com sucesso
            if device(text='Sua privacidade online').exists:
                mensagem_normal(' VPN conectada.')
                device.press('home')
                sleep(velocidade_bot)
                break

            sleep(1)

        return True
    except:
        return False
