from random import choice
from time import sleep

from mensagens.mensagens import mensagem_erro, mensagem_normal
from utils.gerar_dados_perfil import gerar_dados_perfil


def pegar_email(device, velocidade_bot):
    try:
        genero = '1'
        _, usuario = gerar_dados_perfil(genero)

        # Limpar dados do Temp Mail
        device.app_clear('io.tempmail.android')

        # Abrir Temp Mail
        device.app_start('io.tempmail.android', use_monkey=True)
        sleep(velocidade_bot)
        mensagem_normal(' Iniciando o Temp Mail.')

        # CLicar em CHOOSE
        mensagem_normal(' Criando um email temporário.')
        if device(text='CHOOSE').exists(30):
            device(text='CHOOSE').click()
        else:
            device.app_stop('io.tempmail.android')

            # Abrir Temp Mail
            device.app_start('io.tempmail.android', use_monkey=True)

            if device(text='CHOOSE').exists(30):
                device(text='CHOOSE').click()
            else:
                return False

        sleep(velocidade_bot)

        #  clicar em name
        device(text='Name').wait(30)
        device(text='Name').click()
        device(focused=True).set_text(str(usuario))
        sleep(velocidade_bot)

        # Escolher domínio
        dominio = ['vvatxiy.com', 'somelora.com', 'zlorkun.com']
        seletor = choice(dominio)
        device(resourceId='android:id/text1').wait(30)
        device(resourceId='android:id/text1').click()
        sleep(velocidade_bot)
        device(text=seletor).wait(30)
        device(text=seletor).click()
        sleep(velocidade_bot)

        # Clicar em CREATE
        device(text='CREATE').wait(30)
        device(text='CREATE').click()
        sleep(velocidade_bot)

        # Coletar o email criado
        device(resourceId='io.tempmail.android:id/currentEmailTV').wait(30)
        email = device(
            resourceId='io.tempmail.android:id/currentEmailTV').get_text()
        mensagem_normal(' Email temporário criado: ' + email)

        return email
    except:
        return False


def pegar_codigo(device, velocidade_bot):
    try:
        # Abrir Temp Mail
        device.app_start('io.tempmail.android', use_monkey=True)
        sleep(velocidade_bot)

        # Clicar no Mailbox
        mensagem_normal(' Aguardando caixa de entrada do 2NR.')
        device(description='Mailbox').wait(30)
        device(description='Mailbox').click()

        # Se aparecer REFRESH, clica
        caixa_entrada = False
        for _ in range(30):

            # REFRESH
            if device(text='REFRESH').exists:
                device(0.501, 0.589)

            # Se aparecer mensagem na caixa de entrada, coleta e para
            if device(text='Mobilelabs Sp. z o.o. ').exists:
                mensagem_normal(' A caixa de entrada do 2nr chegou.')
                device(text='Mobilelabs Sp. z o.o. ').click()
                caixa_entrada = True
                break

            sleep(1)
        if not caixa_entrada:
            return False

        sleep(velocidade_bot)

        # Clicar no brave
        mensagem_normal(' Abrindo o Brave.')
        for x in range(30):

            if device(text='Kliknij aby aktywować konto').exists:
                mensagem_normal(' Clicando no link do 2nr.')
                device(text='Kliknij aby aktywować konto').click()

            if device(text='Abrir com Brave').exists:
                device(text='Só uma vez').click()
                break
            if device(text='Brave').exists:
                device(text='Brave').click()
                break

            sleep(1)

        # Configura o brave
        device(text='Não agora').wait(30)
        device(text='Não agora').click()
        sleep(velocidade_bot)

        # Continuar
        device(text='Continuar').wait(30)
        device(text='Continuar').click()
        sleep(velocidade_bot)

        sleep(4)
        device.app_clear('com.brave.browser')
        mensagem_normal(' Conta 2NR ativada com sucesso!')

        return True
    except:
        return False
