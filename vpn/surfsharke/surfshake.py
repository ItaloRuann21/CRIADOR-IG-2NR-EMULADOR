
from time import sleep

from mensagens.mensagens import mensagem_atencao, mensagem_normal
from vpn.surfsharke.paises import pais_aleatorio


def conectar_surfshake(device, velocidade_bot):
    try:
        mensagem_atencao(' Iniciando a SurfSharke VPN')
        # Digitar um pais da america sul/norte aleatorio
        paises = pais_aleatorio()

        print(f'País escolhido: {paises}')

        # Entrar SurfShake
        device.app_start('com.surfshark.vpnclient.android', use_monkey=True)
        sleep(velocidade_bot)

        for x in range(30):

            # Verificar se a vpn está conectada, Se tiver desconecta
            if device(text='Desconectar').exists:
                device(text='Desconectar').click()

            # Se aparecer os minutos, clica novamente em desconectar
            if device(text='Experimente Pausar para um intervalo rápido').exists:
                device(text='Desconectar').click()

            # Se caso apareça conexão rápida, então não está conectado.
            if device(text='Conexão rápida').exists:
                break
            sleep(1)
        sleep(velocidade_bot)

        # Pesquisar o pais escolhido:
        if device(className="android.widget.EditText").wait(30):
            device(className="android.widget.EditText").click()
            device(className="android.widget.EditText").set_text(paises)
            sleep(velocidade_bot)

        # Se aparecer isso
        if device(text='Nenhum resultado').exists:
            device(text='Malásia').click()
        else:
            device(className='android.widget.TextView')[1].wait(30)
            device(className='android.widget.TextView')[1].click()
            sleep(velocidade_bot)

         # Se aparecer para solicitar a conexão, clica em OK
        for x in range(30):

            # Confirmar conexão
            if device(text='Solicitação de conexão').exists:
                device(text='OK').click()

            # Se aparecer mensagem de sobreposição de tela
            if device(text='Desativar a otimização de bateria para a Surfshark').exists:
                device(text='Desligar').click()

            # Clica em permitir
            if device(text='PERMITIR').exists:
                device(text='PERMITIR').click()

            # Verificar se conectou com sucesso
            if device(text='Pausar').exists:
                mensagem_normal(' VPN conectada.')
                device.press('home')
                sleep(velocidade_bot)
                break

            sleep(1)

        return True
    except Exception as erro:
        print(erro)
        device
        return False
