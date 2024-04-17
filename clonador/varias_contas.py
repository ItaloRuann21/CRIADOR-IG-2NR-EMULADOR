from time import sleep

from clonador.permissoes_varias_contas import \
    aceitando_permissoes_varias_contas
from Images.ManipularImagens import Imagem
from mensagens.mensagens import mensagem_normal


def configurar_varias_contas(device, velocidade_bot):
    try:

        mensagem_normal('> Limpando dados do Clonador.')
        # Limpar dados clonador varias contas
        device.app_clear('com.excelliance.multiaccounts')
        sleep(velocidade_bot)

        mensagem_normal('> Permissões liberadas, iniciando clonador.')
        # Permitindo todas as permissoes do varias contas,
        aceitando_permissoes_varias_contas(device)
        sleep(velocidade_bot)

        # Abrindo Varias contas
        device.app_start('com.excelliance.multiaccounts', use_monkey=True)
        sleep(velocidade_bot)

        # AGREEND AND CONTINUE
        device(resourceId='com.excelliance.multiaccounts:id/tv_agree').wait(30)
        device(resourceId='com.excelliance.multiaccounts:id/tv_agree').click()
        sleep(velocidade_bot)

        # Clicando No icone para adicionar Instagram
        device(resourceId='com.excelliance.multiaccounts:id/add_but').wait(30)
        device(resourceId='com.excelliance.multiaccounts:id/add_but').click()
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

        for x in range(30):

            # Criar nova conta via texto
            if device(text='Criar nova conta').exists:
                device(text='Criar nova conta').click()
                mensagem_normal('> Instagram clonado!')
                break

            # Criar nova conta via Description
            if device(description='Criar nova conta').exists:
                device(description='Criar nova conta').click()
                mensagem_normal('> Instagram clonado!')
                break

            # Criar nova conta por classe
            if device(className='android.widget.Button')[2].exists:
                device(className='android.widget.Button')[2].click()
                mensagem_normal('> Instagram clonado!')
                break
            sleep(1)

        else:

            # Forçar parada
            device.app_stop('com.excelliance.multiaccounts')
            sleep(velocidade_bot)

            # Abrindo Varias contas
            device.app_start('com.excelliance.multiaccounts', use_monkey=True)
            sleep(velocidade_bot)

            # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
            for x in range(4):

                if device(text='Instagram').exists:
                    device(text='Instagram').click()
                    sleep(velocidade_bot)

                sleep(0.5)

            if device(text='Instagram').exists(timeout=30):
                device(text='Instagram').click()
                sleep(velocidade_bot)

            for x in range(30):

                # Criar nova conta via texto
                if device(text='Criar nova conta').exists:
                    device(text='Criar nova conta').click()
                    mensagem_normal('> Instagram clonado!')
                    break

                # Criar nova conta via Description
                if device(description='Criar nova conta').exists:
                    device(description='Criar nova conta').click()
                    mensagem_normal('> Instagram clonado!')
                    break

                # Criar nova conta por classe
                if device(className='android.widget.Button')[2].exists:
                    device(className='android.widget.Button')[2].click()
                    mensagem_normal('> Instagram clonado!')
                    break
                sleep(1)

        return True
    except Exception as erro:
        print(erro)
        return False
