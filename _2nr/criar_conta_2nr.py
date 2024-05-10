from time import sleep

from _2nr.permissoes_2nr import aceitando_permissoes_2nr
from mensagens.mensagens import mensagem_erro, mensagem_normal


def logar_no_2nr(device, velocidade_bot, email):
    try:

        # Parar 2nr
        device.app_stop('pl.rs.sip.softphone.newapp')

        # Abrir 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
        sleep(velocidade_bot)
        mensagem_normal(' Iniciando o 2NR.')

        # Clicar em Login
        device(text='LOGIN').wait(30)
        device(text='LOGIN').click()
        sleep(velocidade_bot)
        mensagem_normal(' Logando no 2NR.')

        # Clicar em Email e digitar email
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputEmail').wait(30)
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputEmail').click()
        device(focused=True).set_text(str(email))
        sleep(velocidade_bot)

        # Clicar na senha e digitar a senha
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputPassword').wait(30)
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputPassword').click()
        device(focused=True).set_text('italoRuan3257!')
        sleep(velocidade_bot)

        # Clicar em Login
        device(text='LOG IN').wait(30)
        device(text='LOG IN').click()
        mensagem_normal(' Logado com sucesso no 2NR.')

        return True
    except:
        return False


def criar_conta_2nr(device, velocidade_bot, email):
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

        # Clicar em REGISTRATION
        mensagem_normal(' Registrando uma nova conta 2NR.')
        device(text='REGISTRATION').wait(30)
        device(text='REGISTRATION').click()
        sleep(velocidade_bot)

        # Digitar o email
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputEmail').wait(30)
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputEmail').click()
        device(focused=True).set_text(str(email))
        sleep(velocidade_bot)

        # Digitar senha
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputPassword').wait(30)
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputPassword').click()
        device(focused=True).set_text(str('italoRuan3257!'))
        sleep(velocidade_bot)

        # Repetir senha
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputRepeatPassword').wait(30)
        device(resourceId='pl.rs.sip.softphone.newapp:id/inputRepeatPassword').click()
        device(focused=True).set_text(str('italoRuan3257!'))

        # Clicar no checkbox
        device(className='android.widget.CheckBox').wait(30)
        device(className='android.widget.CheckBox').click()

        # Clicar em SIGN UP
        device(text='SIGN UP').wait(30)
        device(text='SIGN UP').click()

        # Se aparecer isso A link to activate your account has been sent to the email address you provided
        if device(text='A link to activate your account has been sent to the email address you provided').wait(30):
            return True
        mensagem_normal(' Conta registrada, esperando ativação.')

    except:
        return False
