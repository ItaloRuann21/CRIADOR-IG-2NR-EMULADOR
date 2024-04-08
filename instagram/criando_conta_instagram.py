from random import randint
from time import sleep

from colorama import Back, Fore, Style, init

from _2nr.pegar_codigo import pegar_codigo
from contas import contas_criadas, nao_criou
from Images.ManipularImagens import Imagem
from mensagens.mensagens import (mensagem_atencao, mensagem_erro,
                                 mensagem_normal, mensagem_sucesso)

# Iniciando contador
contador_contas = 0


def iniciando_criacao_instagram(device, numero, senha, nome, usuario):
    try:

        global contador_contas

        # # Limpar memoria ram
        # device.press('control + shift + t')

        # Instancia de Imagem para manipular
        imagem = Imagem(device)

        # Clicar em Adicionar numero 2nr
        try:
            mensagem_normal('> Adicionando número 2nr')
            device(className='android.widget.EditText')[0].wait(30)
            device(className='android.widget.EditText')[0].click()
        except:
            mensagem_erro(
                '> Não foi possível clicar no campo do input e adicionar o número')
            return False

        # Preecnher numero
        if device(focused=True).exists:
            device(focused=True).set_text(numero)
            mensagem_normal('< Número preenchido.')
            mensagem_normal('< Aguarde!')

        sleep(2)

        # Clicar em Avançar
        device(text='Avançar').wait(30)
        device(text='Avançar').click()

        sleep(2)

        # se aparecer a msg de erro
        if device(text='A Página não está disponível no momento').exists(timeout=5):
            device(text='Recarregar')
            sleep(2)
            device.swipe(0.498, 0.283, 0.501, 0.892)

        # Clicar em Criar nova conta
        try:
            device(text='Criar nova conta').wait(15)
            device(text='Criar nova conta').click()

        except:
            pass

        # se aparecer a msg de erro
        if device(text='A Página não está disponível no momento').exists(timeout=5):
            device(text='Recarregar')
            sleep(2)
            device.swipe(0.498, 0.283, 0.501, 0.892)

        sleep(2)

        # Se aparecer Ocorreu um erro. Tente novamente mais tarde.
        if device(text='Ocorreu um erro. Tente novamente mais tarde.').exists(timeout=5):
            mensagem_atencao(
                '> Erro no número. Trocando IP.')
            return False

        sleep(2)

        mensagem_normal('> Código enviado, esperando.')
        # Instanciando função para pegar codigo
        codigo = False
        codigo = pegar_codigo(device)
        mensagem_normal('> Código chegou: ' + str(codigo))

        if not codigo:
            return 1

        sleep(2)

        # Caso apareça o codigo de confirmação, digita o codigo
        device(text='Código de confirmação').wait(30)
        if device(focused=True).exists:
            device(focused=True).set_text(codigo)
            mensagem_normal('> Código adicionado no input')

        sleep(2)

        # Clicar em avançar
        try:
            device(text='Avançar').wait(30)
            device(text='Avançar').click()
        except:
            pass

        sleep(2)

        # Colocando a senha
        try:
            imagem.clicar_na_imagem('./Images/senha_visivel.png')
            device(focused=True).set_text(senha)
            mensagem_normal('> Senha adicionada no campo do input.')
        except:
            mensagem_erro('> Não foi possível adicionar senha')
            return False

        sleep(2)

        # Clicar em avançar
        device(text='Avançar').wait(10)
        device(text='Avançar').click()
        sleep(2)

        mensagem_normal('> Verificando se existe uma conta com esse número.')
        imagem.clicar_na_imagem(
            './Images/instagram/clicar_criar_nova_conta.png')

        # Clicar em Agora não
        try:
            device(text='Agora não').wait(10)
            device(text='Agora não').click()
        except:
            pass

        sleep(2)

        # Clicar em DEFINIR
        if device(text='DEFINIR').wait(30):
            device(text='DEFINIR').click()
        else:
            imagem.clicar_na_imagem('./Images/definir.png')

        sleep(2)

        # Clicar em avançar
        try:
            device(text='Avançar').wait(30)
            device(text='Avançar').click()
        except:
            pass

        sleep(2)

        # Se aparecer o erro
        if device(text='Parece que você inseriu informações incorretas. Use sua data de nascimento verdadeira.').wait(30):
            device(text='Avançar').wait(30)
            device(text='Avançar').click()

        sleep(2)

        # Definindo o ano
        mensagem_normal('> Definindo idade')
        ano = randint(18, 60)
        device(className='android.widget.EditText').wait(30)
        device(className='android.widget.EditText').set_text(str(ano))

        sleep(2)

        # Clicando em avançar
        device(text='Avançar').wait(30)
        device(text='Avançar').click()

        sleep(2)

        # Se aparecer essa msg
        device(text='OK').wait(30)
        device(text='OK').click()

        sleep(2)

        # Definindo o nome completo
        mensagem_normal('> Digitando o nome completo.')
        imagem.clicar_na_imagem('./Images/nome_completo.png')
        device(focused=True).set_text(nome)
        mensagem_normal('> Nome completo: ' + nome)

        sleep(2)

        # Clicar em avançar
        device(text='Avançar').wait(30)
        device(text='Avançar').click()

        sleep(2)

        # Caso o usuário ja exista...
        seletor = f'O nome de usuário {usuario} não está disponível.'
        if device(text=seletor).exists(5):
            device(className='android.view.ViewGroup')[0].click()
            mensagem_atencao('> Número de usuário já existe! Tentando outro.')

        else:
            # Escolher nome de usuario
            device(className='android.widget.EditText').wait(10)
            usuario = device(className='android.widget.EditText').get_text()
            mensagem_normal('> Nome de usuário definido: ' + usuario)

        sleep(2)

        # Clicar em avançar
        device(text='Avançar').wait(30)
        device(text='Avançar').click()

        sleep(2)

        # Confirmar termos de uso
        mensagem_normal('> Concordando com os termos de uso.')

        # Concordo
        imagem.clicar_na_imagem('./Images/concordo.png')
        if device(text='Concordo').exists(timeout=30):
            imagem.clicar_na_imagem('./Images/concordo.png')

            if device(text='Concordo').exists(timeout=30):
                imagem.clicar_na_imagem('./Images/concordo.png')

        sleep(2)

        # Se apareceu isso, a conta foi criada!
        criou = False
        for x in range(60):
            sleep(1)
            if device(text='Fazer uma apelação').exists:
                mensagem_erro('> NÃO CRIOU. CONTA SUSPENSA!')
                device.app_clear('com.excelliance.multiaccounts')
                criou = False
                return 3

            if device(text='Adicione uma foto do perfil').exists:
                mensagem_sucesso('> CONTA CRIADA COM SUCESSO!')
                contador_contas += 1
                print(Fore.YELLOW + 'Quantidade criadas: ' + Style.RESET_ALL +
                      Fore.GREEN + str(contador_contas) + Style.RESET_ALL)
                contas_criadas(usuario, senha)
                device.app_clear('com.excelliance.multiaccounts')
                criou = True
                return 3

            if device(text='Adicionar foto').exists:
                mensagem_sucesso('> CONTA CRIADA COM SUCESSO!')
                contador_contas += 1
                print(Fore.YELLOW + 'Quantidade criadas: ' + Style.RESET_ALL +
                      Fore.GREEN + str(contador_contas) + Style.RESET_ALL)
                contas_criadas(usuario, senha)
                device.app_clear('com.excelliance.multiaccounts')
                criou = True
                return 3

            if device(text='Pular').exists:
                mensagem_sucesso('> CONTA CRIADA COM SUCESSO!')
                contador_contas += 1
                print(Fore.YELLOW + 'Quantidade criadas: ' + Style.RESET_ALL +
                      Fore.GREEN + str(contador_contas) + Style.RESET_ALL)
                contas_criadas(usuario, senha)
                device.app_clear('com.excelliance.multiaccounts')
                criou = True
                return 3

        if not criou:
            mensagem_erro(
                '> Conta não foi criada! Verifique manualmente depois.')
            nao_criou(usuario, senha)
            return False

        return True
    except Exception as erro:
        print(erro)
        return False
