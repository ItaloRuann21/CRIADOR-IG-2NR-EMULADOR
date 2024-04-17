
from time import sleep

from mensagens.mensagens import mensagem_erro, mensagem_normal


def reinviar_codigo(device, velocidade_bot):
    try:
        device.press('recent')
        sleep(1)
        device.press('recent')

        # Clicar em Não recebi o código
        sleep(velocidade_bot)
        resposta = device(text='Não recebi o código').exists(timeout=30)
        if resposta:
            device(text='Não recebi o código').click()
        else:
            return False
        sleep(velocidade_bot)

        # Clicar em Reenviar código de confirmação
        resposta = device(
            text='Reenviar código de confirmação').exists(timeut=30)
        if resposta:
            device(text='Reenviar código de confirmação').click()
        else:
            return False
        sleep(velocidade_bot)

        # Código de confirmação reenviado
        resposta = device(
            text='Código de confirmação reenviado').exists(timeout=10)
        if resposta:
            mensagem_normal('> Código reinviado. Voltando ao 2nr.')
        else:
            mensagem_erro('> Erro ao reinviar o código.')
            return 1
        sleep(velocidade_bot)

        return True
    except:
        return False
