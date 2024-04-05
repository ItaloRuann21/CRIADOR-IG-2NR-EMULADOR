from time import sleep

from mensagens.mensagens import mensagem_erro, mensagem_normal

from .permissoes_2nr import aceitando_permissoes_2nr


def apagar_conta_2nr(device):
    try:

        mensagem_normal('> Limpando dados do 2NR')

        # Limpar dados 2nr
        try:
            device.app_clear('pl.rs.sip.softphone.newapp')
            mensagem_normal('> Dados limpos com sucesso!')
        except:
            mensagem_erro('> Não foi possível limpar dados do 2NR')

        # Aceitando permissões 2nr
        mensagem_normal('> Permissões do 2nr aceitas com sucesso!')
        aceitando_permissoes_2nr(device)

        # Abrir 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)

        # Clicando em Login
        mensagem_normal('> Fazendo login no 2nr')
        if device(text='LOGIN').exists(timeout=30):
            device(text='LOGIN').click()
        sleep(1)

        # Clicar em Google
        if device(text='Google').exists(timeout=30):
            device(text='Google').click()

        # Escolher a primeira conta
        if device(resourceId='com.google.android.gms:id/account_name').wait(30):
            device(resourceId='com.google.android.gms:id/account_name').click()

        # Clicando em configurações
        mensagem_normal('> Deletando conta 2nr.')
        if device(description='Settings').exists(timeout=30):
            device(description='Settings').click()

        # Deletar conta
        if device(text='Delete account').exists(timeout=30):
            device(text='Delete account').click()
            if device(text='Yes').exists(timeout=30):
                device(text='Yes').click()

        mensagem_normal('> Conta deletada com sucesso.')

        return True
    except Exception as erro:
        print(erro)
        return False
