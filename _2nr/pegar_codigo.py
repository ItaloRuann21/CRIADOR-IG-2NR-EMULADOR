from time import sleep


def pegar_codigo(device, velocidade_bot):
    try:
        # Parar 2nr
        device.app_stop('pl.rs.sip.softphone.newapp')

        # Abrir 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
        sleep(velocidade_bot)

        # Clicando na aba de navegação de mensagens
        seletor = 'pl.rs.sip.softphone.newapp:id/messages'
        device(resourceId=seletor).wait(30)
        device(resourceId=seletor).click()
        sleep(velocidade_bot)

        # Coletando codigo
        seletor = 'pl.rs.sip.softphone.newapp:id/message'
        device(resourceId=seletor).wait(20)
        seletor = 'pl.rs.sip.softphone.newapp:id/message'
        teste = device(
            resourceId='pl.rs.sip.softphone.newapp:id/message').get_text().strip()
        part1 = teste.split(' ')[6]
        part2 = teste.split(' ')[7]
        codigo = part1 + part2.replace('.', '')
        sleep(velocidade_bot)

        # Clicar na engrenagem de confdiguração
        device(
            resourceId='pl.rs.sip.softphone.newapp:id/buttonSettings').wait(30)
        device(
            resourceId='pl.rs.sip.softphone.newapp:id/buttonSettings').click()
        sleep(velocidade_bot)

        # Remover todas as msg
        device(text='Remove all messages').wait(30)
        device(text='Remove all messages').click()
        sleep(velocidade_bot)

        # Voltando ao Varias contas
        device.press('recent')
        sleep(3)
        device.press('recent')
        sleep(velocidade_bot)

        # # Clica na posição x e y da tela para voltar ao instagram
        # device(description='Várias contas (Várias contas)').click()

        return codigo

    except:
        return False
