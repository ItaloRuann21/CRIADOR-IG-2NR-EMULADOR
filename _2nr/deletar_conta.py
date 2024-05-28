from time import sleep

from mensagens.mensagens import mensagem_erro, mensagem_normal


def deletar_conta(device, velocidade_bot):
    try:
        # Clicando em configurações
        device.press('back')
        sleep(3)
        mensagem_normal(' Deletando conta 2nr.')
        if device(description='Settings').exists(timeout=30):
            device(description='Settings').click()
        else:
            mensagem_erro(' Não foi possível clicar em configurações.')
            return False
        sleep(velocidade_bot)

        # Deletar conta
        if device(text='Delete account').exists(timeout=30):
            device(text='Delete account').click()
            if device(text='Yes').exists(timeout=30):
                device(text='Yes').click()
        else:
            mensagem_erro(' Erro ao tentar deletar a conta.')
            return False
        sleep(velocidade_bot)

        mensagem_normal(' Conta 2nr deletada com sucesso.')

        return True
    except:
        return False
