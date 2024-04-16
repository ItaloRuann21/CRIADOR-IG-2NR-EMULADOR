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

        # Clicar em Adicionar numero 2nr
        mensagem_normal('> Adicionando número 2nr')
        resposta = device(description='Número do celular').exists(timeout=30)
        if resposta:
            device(description='Número do celular').click()
        else:
            mensagem_erro(
                '> Não foi possível identificar o elemento de número 2nr. Pagina indisponível.')
            return False

        # Preecnher numero
        resposta = device(focused=True).exists(timeout=30)
        if resposta:
            device(focused=True).set_text(numero)
            mensagem_normal('< Número preenchido.')
        else:
            mensagem_erro('> Não foi possivel preencher número.')
            return False

        # Clicar em Avançar
        def avançar():
            resposta = device(text='Avançar').exists(timeout=30)
            if resposta:
                device(text='Avançar').click()
            else:
                mensagem_erro('> Não clicou em avançar.')
                return False
        avançar()

        # Você está tentando entrar?
        resposta = device(text='Criar nova conta').exists(timeout=30)
        if resposta:
            mensagem_normal('> Clicando em Criar nova conta.')
            device(text='Criar nova conta').click()

        # Se aparecer Ocorreu um erro. Tente novamente mais tarde.
        if device(text='Ocorreu um erro. Tente novamente mais tarde.').exists(timeout=7):
            mensagem_atencao(
                '> Erro no número. Trocando IP.')
            return False

        mensagem_normal('> Código enviado, esperando.')
        # Instanciando função para pegar codigo
        codigo = False
        codigo = pegar_codigo(device)
        if codigo:
            mensagem_normal('> Código chegou: ' + str(codigo))
        if not codigo:
            mensagem_erro('> Código não chegou no 2nr.')
            return 1

        # Caso apareça o codigo de confirmação, digita o codigo
        resposta = device(text='Código de confirmação').exists(timeout=30)
        if resposta:
            device(focused=True).set_text(codigo)
            mensagem_normal('> Código adicionado no input')
        else:
            mensagem_erro('> Não foi possível adicionar o código.')
            return False

        # Clicar em Avançar
        avançar()

        # Colocando a senha
        resposta = device(focused=True).exists(timeout=30)
        if resposta:
            device(focused=True).set_text(senha)
            mensagem_normal('> Senha adicionada no campo do input.')
        else:
            mensagem_erro('> Não foi possível adicionar senha')
            return False

        # Clicar em Avançar
        avançar()

        # Verificando se existe uma conta com esse número.
        resposta = device(text='CRIAR NOVA CONTA').exists(timeout=7)
        if resposta:
            device(text='CRIAR NOVA CONTA').click()

        # Salvar suas informações de login?
        resposta = device(
            text='Salvar suas informações de login?').exists(timeout=30)
        if resposta:
            device(text='Agora não').click()

        # Clicar em DEFINIR
        resposta = device(text='DEFINIR').exists(timeout=30)
        if resposta:
            device(text='DEFINIR').click()
        else:
            mensagem_erro('> Erro ao clicar em DEFINIR')
            return False

        # Clicar em avançar
        avançar()

        # Se aparecer o erro
        resposta = device(
            text='Parece que você inseriu informações incorretas. Use sua data de nascimento verdadeira.').exists(timeout=30)
        if resposta:
            device(text='Avançar').click()
        else:
            mensagem_erro('> Erro ao clicar em avançar')
            return False

        # Definindo o ano
        mensagem_normal('> Definindo idade')
        ano = randint(18, 60)
        resposta = device(
            className='android.widget.EditText').exists(timeout=30)
        if resposta:
            device(className='android.widget.EditText').set_text(str(ano))
        else:
            mensagem_erro('> Não adicionou a idade no input.')
            return False

        # Clicando em avançar
        avançar()

        # Se aparecer essa msg
        resposta = device(text='OK').exists(timeout=30)
        if resposta:
            device(text='OK').click()
        else:
            mensagem_erro('> Não clicou em OK')
            return False

        # Definindo o nome completo
        mensagem_normal('> Digitando o nome completo.')
        resposta = device(focused=True).exists(timeout=30)
        if resposta:
            device(focused=True).set_text(nome)
            mensagem_normal('> Nome completo: ' + nome)
        else:
            mensagem_erro(
                '> Não foi possível adicionar o nome completo no input')
            return False

        # Clicar em avançar
        avançar()

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

        # Clicando em avançar
        avançar()

        # Confirmar termos de uso
        mensagem_normal('> Concordando com os termos de uso.')

        # Se apareceu isso, a conta foi criada!
        criou = False
        for x in range(60):

            # Clicando em concordo
            if device(text='Concordo').exists:
                device(text='Concordo').click()

            if device(text='Fazer uma apelação').exists:
                mensagem_erro('> NÃO CRIOU. CONTA SUSPENSA!')
                device.app_clear('com.excelliance.multiaccounts')
                criou = False
                return 2

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

            sleep(1)

        if not criou:
            mensagem_erro(
                '> Conta não foi criada! Verifique manualmente depois.')
            nao_criou(usuario, senha)
            return False

        return True
    except Exception as erro:
        print(erro)
        return False
