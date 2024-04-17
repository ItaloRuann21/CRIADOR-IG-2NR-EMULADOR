from time import sleep


def pegar_codigo(device, velocidade_bot):
    try:
        # Abrir 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
        sleep(velocidade_bot)

        # Clicando na mensagem
        seletor = '//*[@resource-id="pl.rs.sip.softphone.newapp:id/messages"]/android.widget.FrameLayout[1]'
        if device.xpath(seletor).wait(60):
            device.xpath(seletor).click()
            sleep(velocidade_bot)

            # Coletando codigo
            seletor = '//*[@resource-id="pl.rs.sip.softphone.newapp:id/message"]'
            if device.xpath(seletor).wait(30):
                codigo_encontrado = device.xpath(seletor)
                codigo_texto = codigo_encontrado.get_text()
                codigo_split = codigo_texto.split(' ')
                codigo_part1 = codigo_split[6]
                codigo_part2 = codigo_split[7]
                codigo_novo = codigo_part1 + codigo_part2
                codigo = codigo_novo.replace('.', '')
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
                sleep(velocidade_bot)

                # Clica na posição x e y da tela para voltar ao instagram
                device(description='Várias contas (Várias contas)').click()

                return codigo
        else:

            # Se não foi possível encontrar o código, lidar com essa situação
            # Forçar parada do 2nr
            device.app_stop('pl.rs.sip.softphone.newapp')
            sleep(velocidade_bot)

            # Abrir 2nr
            device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
            sleep(velocidade_bot)

            # Clicar em mensagens
            device(resourceId='pl.rs.sip.softphone.newapp:id/messages').wait(30)
            device(resourceId='pl.rs.sip.softphone.newapp:id/messages').click()
            sleep(velocidade_bot)

        return False
    except:
        return False
