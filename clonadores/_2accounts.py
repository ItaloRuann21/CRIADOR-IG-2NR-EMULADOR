from time import sleep

from clonadores.permissoes_2accounts import aceitando_permissoes_2accounts
from mensagens.mensagens import mensagem_normal


def configurar_2_accounts(device, velocidade_bot):
    try:

        mensagem_normal(' Limpando dados do Clonador.')
        # Limpar dados clonador varias contas
        device.app_clear('com.excelliance.multiaccount')
        sleep(velocidade_bot)

        mensagem_normal(' Permissões liberadas, iniciando clonador.')
        # Permitindo todas as permissoes do varias contas,
        aceitando_permissoes_2accounts(device)
        sleep(velocidade_bot)

        # Abrindo 2accounts
        device.app_start('com.excelliance.multiaccount', use_monkey=True)
        sleep(velocidade_bot)

        # AGREEND AND CONTINUE
        device(resourceId='com.excelliance.multiaccount:id/tv_agree').wait(30)
        device(resourceId='com.excelliance.multiaccount:id/tv_agree').click()
        sleep(velocidade_bot)

        # Clicando No icone para adicionar Instagram
        device(resourceId='com.excelliance.multiaccount:id/add_but').wait(30)
        device(resourceId='com.excelliance.multiaccount:id/add_but').click()
        sleep(velocidade_bot)

        # Clicar no Instagram
        device(text='Instagram').wait(30)
        device(text='Instagram').click()
        sleep(velocidade_bot)

        # Se aparecer essa mensage, clica em OK
        seletor = 'Para que Instagram seja executado corretamente, conceda estas permissões: • Telefone'
        device(text=seletor).wait(30)
        device(text='OK').click()
        sleep(velocidade_bot)

        # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
        for x in range(30):

            if device(text='Instagram').exists:
                device(text='Instagram').click()

            if device(text='Criar nova conta').exists:
                device(text='Criar nova conta').click()
                return True

            sleep(1)

        else:

            # Forçar parada
            device.app_stop('com.excelliance.multiaccount')
            sleep(velocidade_bot)

            # Abrindo Varias contas
            device.app_start('com.excelliance.multiaccount', use_monkey=True)
            sleep(velocidade_bot)

            # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
            for x in range(30):

                if device(text='Instagram').exists:
                    device(text='Instagram').click()

                if device(text='Criar nova conta').exists:
                    device(text='Criar nova conta').click()
                    return True

                sleep(1)

            # sleep(velocidade_bot)

            # # Criar nova conta via texto
            # if device(text='Criar nova conta').exists(timeout=30):
            #     device(text='Criar nova conta').click()
            #     mensagem_normal(' Instagram clonado!')
            #     return True

        return True
    except Exception as erro:
        print(erro)
        return False
