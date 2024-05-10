from time import sleep

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

        # CLicar em CHOOSE
        device(text='CHOOSE').wait(30)
        device(text='CHOOSE').click()
        sleep(velocidade_bot)

        #  clicar em name
        device(text='Name').wait(30)
        device(text='Name').click()
        device(focused=True).set_text(str(usuario))
        sleep(velocidade_bot)

        # Escolher domínio
        dominio = 'vvatxiy.com'
        device(resourceId='android:id/text1').wait(30)
        device(resourceId='android:id/text1').click()
        sleep(velocidade_bot)
        device(text=dominio).wait(30)
        device(text=dominio).click()
        sleep(velocidade_bot)

        # Clicar em CREATE
        device(text='CREATE').wait(30)
        device(text='CREATE').click()
        sleep(velocidade_bot)

        # Coletar o email criado
        device(resourceId='io.tempmail.android:id/currentEmailTV').wait(30)
        email = device(
            resourceId='io.tempmail.android:id/currentEmailTV').get_text()

        return email
    except:
        return False


def pegar_codigo(device, velocidade_bot):
    try:
        # Abrir Temp Mail
        device.app_start('io.tempmail.android', use_monkey=True)
        sleep(velocidade_bot)

        # Clicar no Mailbox
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
                device(text='Mobilelabs Sp. z o.o. ').click()
                caixa_entrada = True
                break

            sleep(1)
        if not caixa_entrada:
            return False

        sleep(velocidade_bot)
        # Verifica se aparece a mensagem 'Twoje konto w aplikacji 2nr zostało aktywowane'
        device(className='android.webkit.WebView').wait(30)
        caixa_mensagem = device(className='android.webkit.WebView').get_text()
        if caixa_mensagem == 'Twoje konto w aplikacji 2nr zostało aktywowane':
            device.click(0.501, 0.878)
        sleep(velocidade_bot)

        # Clicar em Só uma vez
        device(text='Só uma vez').wait(30)
        device(text='Só uma vez').click()
        sleep(velocidade_bot)

        # Configura o brave
        device(text='Não agora').wait(30)
        device(text='Não agora').click()
        sleep(velocidade_bot)

        # Continuar
        device(text='Continuar').wait(30)
        device(text='Continuar').click()
        sleep(velocidade_bot)

        # Se aparecer esse texto drugi-numer.pl/pl/faq? então a conta do 2nr foi ativada!
        if device(text='drugi-numer.pl/pl/faq?').wait(30):
            device.app_clear('com.brave.browser')

        return True
    except:
        return False
