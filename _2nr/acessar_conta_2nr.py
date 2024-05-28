from time import sleep

from mensagens.mensagens import mensagem_erro, mensagem_normal

from .permissoes_2nr import aceitando_permissoes_2nr


def acessar_conta_2nr(device, velocidade_bot):
    try:

        mensagem_normal(' Limpando dados do 2NR')

        # Limpar dados 2nr
        try:
            device.app_clear('pl.rs.sip.softphone.newapp')
            mensagem_normal(' Dados limpos com sucesso!')
            sleep(velocidade_bot)
        except:
            mensagem_erro(' Não foi possível limpar dados do 2NR')

        # Aceitando permissões 2nr
        mensagem_normal(' Permissões do 2nr aceitas com sucesso!')
        aceitando_permissoes_2nr(device)
        sleep(velocidade_bot)

        # Abrir 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
        sleep(velocidade_bot)

        # Clicando em Login
        mensagem_normal(' Fazendo login no 2nr')
        if device(text='LOGIN').exists(timeout=30):
            device(text='LOGIN').click()
        else:
            mensagem_erro(' Erro ao clicar em LOGIN.')
            return False
        sleep(velocidade_bot)

        # Clicar em Google
        if device(text='Google').exists(timeout=30):
            device(text='Google').click()
        else:
            mensagem_erro(' Erro ao clicar em Google.')
            return False
        sleep(velocidade_bot)

        # Escolher a primeira conta
        if device(resourceId='com.google.android.gms:id/account_name').wait(30):
            device(resourceId='com.google.android.gms:id/account_name').click()
        else:
            mensagem_erro(' Erro ao clicar na primeira conta do google.')
            return False
        sleep(velocidade_bot)

        return True
    except Exception as erro:
        print(erro)
        return False
