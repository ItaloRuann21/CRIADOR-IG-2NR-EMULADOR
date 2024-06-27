from time import sleep


def pegar_codigo(device, velocidade_bot):
    try:
        # Parar 2nr
        device.app_stop('pl.rs.sip.softphone.newapp')

        # Abrir 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
        sleep(velocidade_bot)

        # Clicando na aba de navegação de mensagens
        seletor = 'Messages'
        if device(description=seletor).wait(30):
            device(description=seletor).click()
            sleep(velocidade_bot)

            # Coletando codigo
            seletor = '//*[@resource-id="pl.rs.sip.softphone.newapp:id/message"]'
            if device.xpath(seletor).wait(30):
                seletor = 'pl.rs.sip.softphone.newapp:id/message'
                mensagem = device(resourceId=seletor).get_text()
                codigo = mensagem.split('Instagram e')[1].split('.')[0].replace(' ', '')
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
                sleep(1)
                device.press('recent')
                sleep(velocidade_bot)

                # # Clica na posição x e y da tela para voltar ao instagram
                # device(description='Várias contas (Várias contas)').click()

                return codigo

    except:
        return False
