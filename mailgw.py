from time import sleep
from playwright.sync_api import sync_playwright

from funçoes_playwright.abrir_navegador import abrir_navegador

def email_mailgw(pagina, email, senha):
    try:
        # mailgw
        pagina.goto('https://mail.gw/en/')
        

        # Clicar no menu
        pagina.wait_for_selector('#accounts-menu')
        pagina.click('#accounts-menu')

        # Clicar em Criar conta
        pagina.wait_for_selector('[class="py-1"]')
        seletor = pagina.query_selector_all('[class="py-1"]')[0]
        seletor.click()

        # Digitando email no campo do input
        pagina.wait_for_selector('#username')
        pagina.fill('#username', email)

        # DIgitando senha no campo no input
        pagina.wait_for_selector('#password')
        pagina.fill('#password', senha)

        # Criando email
        pagina.wait_for_selector('[type="button"]')
        pagina.click('[type="button"]')

        # Espere até que o elemento com o ID 'address' esteja pronto
        email_criado = pagina.wait_for_selector('#address')
        pagina.wait_for_timeout(2000)

        # Obtenha o valor do atributo 'value' do elemento usando evaluate
        valor_email = email_criado.evaluate('(element) => element.value')
        
        return valor_email

    except Exception as erro:
        print(erro)
        return False

def codigo_mailgw(pagina):
    try:
        # Esperar código chegar
        pagina.wait_for_selector('[class="all-messages"]', timeout=60000)
        
        # Verificar se existe o nome na caixa de mensagem
        seletor = pagina.query_selector('[class="all-messages"]').text_content()
        
        # Verificar se existe esse dominio do 2nr
        if '<kontakt@2nr.pl>' in seletor:
            # Clicar nas mensagens
            pagina.click('[class="the-message-subject"]')

        
        for x in range(30):
            print('> Esperando chegar a mensagem para clicar no link')
            # Esperando 1 segundo
            pagina.wait_for_timeout(1000)

            # Capturando o botão de substituir e-mail
            resultado = pagina.evaluate('''()=>{
                var res = false
                document.querySelectorAll('u').forEach((u)=>{
                    if(u.innerText == 'Kliknij aby aktywować konto'){
                        u.click()
                        res = true
                    }
                })
                return res
            }''')

            if resultado:
                break
            else:
                return False
        
        # Aguardar a nova página ser aberta
        nova_pagina = pagina.wait_for_event('popup')
        
        # Esperar o seletor chegar
        if nova_pagina.wait_for_selector('[class="hamburger-box"]'):
            print('> Conta 2NR Criada!')
        
        return True

    except Exception as erro:
        print(erro)
        return False
    
with sync_playwright() as playwright:
            navegador, pagina = abrir_navegador(playwright)
            email = email_mailgw(pagina, 'italoflamenddxssasaxsgjuisj344', 'senehdyed44')