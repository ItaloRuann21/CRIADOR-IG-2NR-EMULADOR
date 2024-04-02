from time import sleep

from playwright.sync_api import sync_playwright

from contas import contas_2nr
from funçoes_playwright.abrir_navegador import abrir_navegador
from mensagens.mensagens import (mensagem_erro, mensagem_normal,
                                 mensagem_sucesso)
from tuamae_email import pegar_codigo, pegar_email

from .permissoes_2nr import aceitando_permissoes_2nr


def logando_2nr(device):
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
    
        # Entrar
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)
        sleep(2)
        
        # REGISTRATION
        mensagem_normal('> Criando uma conta do 2nr')
        device(text="REGISTRATION").wait(30)
        device(text="REGISTRATION").click()
        sleep(2)
        
        # Abrir PlayWright
        with sync_playwright() as playwright:
            navegador, pagina = abrir_navegador(playwright)
            email = pegar_email(pagina)
            
            # Add Email
            device(text='E-mail').wait(30)
            device(text='E-mail').click()
            sleep(2)
            device(resourceId='pl.rs.sip.softphone.newapp:id/inputEmailEditText').wait(30)
            device(resourceId='pl.rs.sip.softphone.newapp:id/inputEmailEditText').set_text(email)
            mensagem_normal('> Email 2nr: ' + email)
            
            # Digitar senha
            input_password_element = device(resourceId="pl.rs.sip.softphone.newapp:id/inputPasswordEditText")
            input_password_element.set_text('bot2NRinstagram!')
            mensagem_normal('> Email 2nr: bot2NRinstagram')
            sleep(2)
            
            # Repetir senha
            repeat_password_element = device(resourceId="pl.rs.sip.softphone.newapp:id/repeat_password_edit_text")
            repeat_password_element.set_text('bot2NRinstagram!')
            
            # Confirmar os bagui
            device(resourceId='pl.rs.sip.softphone.newapp:id/checkPrivacyPolicy').wait(30)
            device(resourceId='pl.rs.sip.softphone.newapp:id/checkPrivacyPolicy').click()
            
            # Clicar em Criar
            device(resourceId='pl.rs.sip.softphone.newapp:id/buttonRegister').wait(30)
            device(resourceId='pl.rs.sip.softphone.newapp:id/buttonRegister').click()
            
            # Se aparecer a mensagem de confirmação, clica no link
            seletor = 'A link to activate your account has been sent to the email address you provided'
            if device(text=seletor).wait(30):
                device(text='OK').click()
            else:
                return False
            
            # Pegar codigo
            mensagem_normal('> Esperando chegar a mensagem na caixa de entrada')
            for x in range(30):
                sleep(2)
                res = pegar_codigo(pagina)
                mensagem_normal('> Conta 2nr Ativada!')
                if res:
                    break
            
            navegador.close()
            
        # Fazendo login no 2nr
        mensagem_normal('> Fazendo login no 2nr')
        device(text='Log in').wait(30)
        device(text='Log in').click()
        
        # Email
        device(text='E-mail').wait(30)
        device(text='E-mail').click()
        device(resourceId='pl.rs.sip.softphone.newapp:id/emailEdiText').set_text(email)
        sleep(2)
        
        # Senha
        device(text='Password').wait(30)
        device(text='Password').click()
        device(resourceId='pl.rs.sip.softphone.newapp:id/passwordEdiText').set_text('bot2NRinstagram!')
            
        # Login 
        device(text='LOG IN').wait(30)
        device(text='LOG IN').click()
        
        # Se aparecer o seletor, então login criado!
        if device(text='Balance').exists(timeout=30):
            mensagem_normal('> Login efetuado com sucesso no 2nr')
            contas_2nr(email, 'bot2NRinstagram!')
            return True
        else:
            mensagem_erro('> Não foi possível efeutar o login no 2nr')
            return False
        
        
    except Exception as erro:
        print(erro)
        return False