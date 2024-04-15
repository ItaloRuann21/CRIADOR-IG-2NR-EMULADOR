from time import sleep

from clonador.permissoes_varias_contas import \
    aceitando_permissoes_varias_contas
from Images.ManipularImagens import Imagem
from mensagens.mensagens import mensagem_normal


def configurar_varias_contas(device):
    try:

        mensagem_normal('> Limpando dados do Clonador.')
        # Limpar dados clonador varias contas
        device.app_clear('com.excelliance.multiaccounts')

        mensagem_normal('> Permissões liberadas, iniciando clonador.')
        # Permitindo todas as permissoes do varias contas,
        aceitando_permissoes_varias_contas(device)

        # Abrindo Varias contas
        device.app_start('com.excelliance.multiaccounts', use_monkey=True)

        # AGREEND AND CONTINUE
        device(resourceId='com.excelliance.multiaccounts:id/tv_agree').wait(30)
        device(resourceId='com.excelliance.multiaccounts:id/tv_agree').click()
        sleep(2)

        # Clicando No icone para adicionar Instagram
        device(resourceId='com.excelliance.multiaccounts:id/add_but').wait(30)
        device(resourceId='com.excelliance.multiaccounts:id/add_but').click()
        sleep(2)

        # Clicar no Instagram
        device(text='Instagram').wait(30)
        device(text='Instagram').click()
        sleep(2)

        # Se aparecer essa mensage, clica em OK
        seletor = 'Para que Instagram seja executado corretamente, conceda estas permissões: • Telefone'
        device(text=seletor).wait(30)
        device(text='OK').click()
        sleep(2)

        if device(description='Criar nova conta').exists(30):
            device(description='Criar nova conta').click()
            return True
        else:

            # Forçar parada
            device.app_stop('com.excelliance.multiaccounts')

            # Abrindo Varias contas
            device.app_start('com.excelliance.multiaccounts', use_monkey=True)

            # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
            for x in range(4):

                if device(text='Instagram').exists:
                    device(text='Instagram').click()

                sleep(0.5)

            if device(text='Instagram').exists(timeout=30):
                device(text='Instagram').click()

            if device(description='Criar nova conta').exists:
                device(description='Criar nova conta').click()
                mensagem_normal('> Instagram clonado!')

        return True
    except Exception as erro:
        print(erro)
        return False
