from time import sleep

from funçoes_playwright.abrir_navegador import abrir_navegador


def pegar_email(pagina):
    try:
        
        
        # Tua mae aquela puta
        pagina.goto('https://tuamaeaquelaursa.com/')
        
        # Clicar em Acessar email
        pagina.wait_for_selector('[type="submit"]', timeout=3000)
        pagina.click('[type="submit"]')
        pagina.wait_for_timeout(4000)
        
        # Armazenar email
        pagina.wait_for_selector('[readonly="readonly"]', timeout=3000)
        email = pagina.evaluate('''() =>
            {
                const elemento = document.querySelector('[readonly="readonly"]');
                return elemento.value;
            }
        ''')
        
        return email

    except Exception as erro:
        print(erro)
        return False

def pegar_codigo(pagina):
    try:
        # Esperar código chegar
        pagina.wait_for_selector('[class="all-messages"]', timeout=60)
        
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
