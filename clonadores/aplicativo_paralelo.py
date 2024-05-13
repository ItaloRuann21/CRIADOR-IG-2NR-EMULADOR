from time import sleep

from clonadores.permissoes_paralelo import aceitando_permissoes_app_paralelo
from mensagens.mensagens import mensagem_normal


def configurar_aplicativo_paralelo(device, velocidade_bot):
    try:
        mensagem_normal(' Limpando dados do Clonador.')
        device.app_clear('com.excean.parallelspace')
        sleep(velocidade_bot)

        mensagem_normal(' Permissões liberadas, iniciando clonador.')
        aceitando_permissoes_app_paralelo(device)
        sleep(velocidade_bot)

        # Abrindo aplicativo paralelo
        device.app_start('com.excean.parallelspace', use_monkey=True)
        sleep(velocidade_bot)

        # AGREE AND CONTINUE
        device(resourceId='com.excean.parallelspace:id/tv_agree').wait(30)
        device(resourceId='com.excean.parallelspace:id/tv_agree').click()
        sleep(velocidade_bot)

        # Clique vazio para destravar o clonador
        device(text='Toque aqui para adicionar aplicativos').wait(30)
        device(text='Toque aqui para adicionar aplicativos').click()
        sleep(velocidade_bot)

        # Clicar em Adicionar
        device(text='Adicionar').wait(30)
        device(text='Adicionar').click()
        sleep(velocidade_bot)

        # Clicar em Instagram
        device(text='Instagram').wait(30)
        device(text='Instagram').click()
        sleep(velocidade_bot)

        # Se aparecer mensagem de Observação
        if device(text='Observação').exists(30):
            device(text='OK').click()

        # Se aparecer algum seletor do Instagram, foi clonado com sucesso!
        for x in range(30):

            if device(text='Instagram').exists:
                device(text='Instagram').click()

            if device(text='Criar nova conta').exists:
                device(text='Criar nova conta').click()
                return True
            sleep(1)

        else:

            # Forçar parada
            device.app_stop('com.excean.parallelspace')
            sleep(velocidade_bot)

            # Abrindo Aplicativo paralelo
            device.app_start('com.excean.parallelspace', use_monkey=True)
            sleep(velocidade_bot)

            # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
            for x in range(30):

                if device(text='Instagram').exists:
                    device(text='Instagram').click()

                if device(text='Criar nova conta').exists:
                    device(text='Criar nova conta').click()
                    return True

                sleep(1)

        return True
    except:
        return False
