from time import sleep

import cv2

from clonador.permissoes_varias_contas import \
    aceitando_permissoes_varias_contas
from Images.ManipularImagens import Imagem
from mensagens.mensagens import mensagem_normal, mensagem_sucesso


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

        # Se aparecer anuncio
        mensagem_normal('> Verificando se tem anúncios')
        if device(text='Consent').wait(5):
            device(text='Consent').click()

            # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
            if device(text='Instagram').wait(5):
                device(text='Instagram').click()

        # Se nao iniciar de primeira e aparecer aplicativo do instagram, clica.
        if device(text='Instagram').wait(5):
            device(text='Instagram').click()

        # Verificar se existe o erro de idioma
        if device(text='Continuar em inglês (EUA)').exists(5):
            device(text='Continuar em inglês (EUA)').click()

        # Clicar em Criar nova conta
        device(description='Criar nova conta').wait(35)
        device(description='Criar nova conta').click()
        mensagem_normal('> Instagram clonado!')

        return True
    except Exception as erro:
        print(erro)
        return False
