from time import sleep

from mensagens.mensagens import (mensagem_erro, mensagem_normal,
                                 mensagem_sucesso)
from utils.gerar_nome_numero import nome_do_numero


def criando_numero(device):
    try:

        # Sair do 2nr
        mensagem_normal('> Criando número no 2nr')
        device.app_stop('pl.rs.sip.softphone.newapp')

        # Abre o 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True)

        # Clicando em Login
        mensagem_normal('> Fazendo login no 2nr')
        if device(text='LOGIN').exists(timeout=30):
            device(text='LOGIN').click()

        # Clicar em Google
        if device(text='Google').exists(timeout=30):
            device(text='Google').click()

        # Escolher a primeira conta
        if device(className='android.widget.LinearLayout')[0].exists(timeout=30):
            device(className='android.widget.LinearLayout')[0].click()

        # Clicar no Icone de Criar numero
        try:
            seletor = 'pl.rs.sip.softphone.newapp:id/addNumber'
            device(resourceId=seletor).wait(30)
            device(resourceId=seletor).click()
        except Exception as erro:
            mensagem_erro('> Erro no seletor de Criar número no 2nr')
            print(erro)
            return False

        # Inventar um nome aleatório para o número
        try:
            nome_numero = nome_do_numero()
            seletor = 'android.widget.EditText'
            device(className=seletor)[0].wait(30)
            device(className=seletor)[0].click()
            device(className=seletor).set_text(nome_numero)
        except Exception as erro:
            mensagem_erro('> Erro ao gerar nome aleatório no número')
            print(erro)
            return False

        # Clicar em SAve
        seletor = 'pl.rs.sip.softphone.newapp:id/save'
        device(resourceId=seletor).wait(30)
        device(resourceId=seletor).click()

        #  I agree
        seletor = 'pl.rs.sip.softphone.newapp:id/buttonAgree'
        device(resourceId=seletor).wait(30)
        device(resourceId=seletor).click()

        device(resourceId=seletor).wait(30)
        device(resourceId=seletor).click()

        # Clicar em Save novamente
        seletor = 'pl.rs.sip.softphone.newapp:id/save'
        device(resourceId=seletor).wait(30)
        device(resourceId=seletor).click()

        # Se aparecer a mensagem de verificação com sucesso, então criou o número!
        seletor = 'Successful verification'
        contador = 0
        while contador < 30:
            if device(text=seletor).exists(10):
                device(resourceId='pl.rs.sip.softphone.newapp:id/save').click()
                break
            else:
                device.swipe(0.498, 0.308, 0.508, 0.891)
                contador += 1

        # Se aparecer esse seletor, numero foi criado!
        seletor = 'pl.rs.sip.softphone.newapp:id/phoneNumber'
        device(resourceId=seletor).wait(30)
        if device(resourceId=seletor).exists:  # Se existir o seletor, armazena o número!
            texto_numero = device(resourceId=seletor)
            obter_texto_numero = texto_numero.get_text()
            dividir_numeros = obter_texto_numero.split(' ')
            unir_numeros = ''.join(dividir_numeros)
            numero = '+48' + unir_numeros
            mensagem_normal('> Número criado: ' + numero)

            return numero
        else:
            mensagem_erro('> Erro no 2nr.')
            return False
    except Exception as erro:
        print(erro)
        return False
