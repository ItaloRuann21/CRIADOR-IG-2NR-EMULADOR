
from time import sleep

from mensagens.mensagens import mensagem_atencao
from vpn.surfsharke.paises import pais_aleatorio


def conectar_surfshake(device):
    try:
        mensagem_atencao('> Iniciando a SurfSharke VPN')
        # Digitar um pais da america sul/norte aleatorio
        paises = pais_aleatorio()

        print(f'País escolhido: {paises}')

        # Entrar SurfShake
        device.app_start('com.surfshark.vpnclient.android', use_monkey=True)
        sleep(2)

        # Verificar se a vpn está conectada, Se tiver desconecta
        if device(text='Desconectar').wait(5):
            device(text='Desconectar').click()
        # Pesquisar o pais escolhido:
        if device(className="android.widget.EditText").wait(30):
            device(className="android.widget.EditText").click()
            device(className="android.widget.EditText").set_text(paises)
            sleep(2)

        # Se aparecer isso
        if device(text='Nenhum resultado').exists:
            device(text='Malásia').click()
        else:
            device(className='android.widget.TextView')[1].wait(30)
            device(className='android.widget.TextView')[1].click()
            sleep(2)

        # Se aparecer que conectou
        if device(text='Pausar').wait(10):
            device.press('home')
            return True
        else:
            return False

    except Exception as erro:
        print(erro)
        device
        return False
