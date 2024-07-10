from time import sleep

from mensagens.mensagens import mensagem_normal


def reinviar_codigo(device, velocidade_bot):
    try:
        mensagem_normal(' Reeinviando código.')

        device(text='Não recebi o código').wait(30)
        device(text='Não recebi o código').click()

        sleep(velocidade_bot)

        device(text='Reenviar código de confirmação').wait(30)
        device(text='Reenviar código de confirmação').click()

        sleep(velocidade_bot)

        # Verificar se apareceu mensagem de reenvio
        for _ in range(30):

            if device(text='Código de confirmação reenviado').exists:
                mensagem_normal(' Código reeinviado. Verificando novamente.')
                break

            sleep(1)

        return True
    except:
        return False
