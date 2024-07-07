from random import randint
from time import sleep

from colorama import Back, Fore, Style, init

from _2nr.pegar_codigo import pegar_codigo
from contas import contas_criadas, nao_criou
from utils.criar_conta_bd import create_conta_bd
from mensagens.mensagens import (mensagem_atencao, mensagem_desativada,
                                 mensagem_erro, mensagem_normal,
                                 mensagem_sucesso)

# Iniciando contador
contador_contas = 0


def criar_conta_bd(usuario, senha):
    res = create_conta_bd(usuario, senha)
    if not res:
        res = create_conta_bd(usuario, senha)
        if not res:
            contas_criadas(usuario, senha)


def iniciando_criacao_instagram(device, numero, senha, nome, usuario, velocidade_bot):
    try:

        global contador_contas

        sleep(velocidade_bot)
        # Clicar em Adicionar numero 2nr
        mensagem_normal(' Adicionando número 2nr')
        resposta = False
        for x in range(30):

            if device(description='Número do celular').exists:
                device(className='android.widget.EditText').click()
                resposta = True
                break

            if device(description='Número de celular').exists:
                device(className='android.widget.EditText').click()
                resposta = True
                break

            if device(description='Número de celular ou email').exists:
                device(className='android.widget.EditText').click()
                resposta = True
                break
        if not resposta:
            mensagem_erro(
                ' Não foi possível identificar o elemento de número 2nr. Pagina indisponível.')
            return False

        sleep(velocidade_bot)

        # Preecnher numero
        resposta = device(focused=True).exists(timeout=30)
        if resposta:
            device(focused=True).set_text(numero)

            mensagem_normal(' Número preenchido.')
        else:
            mensagem_erro(' Não foi possivel preencher número.')
            return False
        sleep(velocidade_bot)

        # Clicar em Avançar
        def avançar():
            resposta = device(text='Avançar').exists(timeout=30)
            if resposta:
                device(text='Avançar').click()
            else:
                mensagem_erro(' Não clicou em avançar.')
                return False

        avançar()
        sleep(velocidade_bot)

        for _ in range(30):

            # Se aparecer pagina indisponivel
            if device(text='A Página não está disponível no momento').exists:
                mensagem_normal(
                    ' Pagina indisponível no momento. Resolvendo...')
                device.press('back')
                break

            if device(text='Criar nova conta').exists:
                mensagem_normal(' Clicando em Criar nova conta.')
                device(text='Criar nova conta').click()
                break

            sleep(1)

        # Verificar se existe Confirmar por ligação telefônica
        if device(text='Confirmar por ligação telefônica').exists(timeout=8):
            device(text='Enviar código por SMS').click()

            # Verificar se existre botão de envir código ou avançar
            if device(text='Enviar código').exists(timeout=10):
                device(text='Enviar código').click()
            else:
                avançar()

        sleep(velocidade_bot)

        # Se aparecer Ocorreu um erro. Tente novamente mais tarde.
        if device(text='Ocorreu um erro. Tente novamente mais tarde.').exists(timeout=7):
            mensagem_atencao(
                ' Erro no número. Trocando IP e limpando dados do clonador.')
            return 4
        sleep(velocidade_bot)

        # Verificando campo de código de confirmação
        if device(text='Insira o código de confirmação').exists(timeout=30):
            mensagem_normal(' Código enviado, aguardando.')
            tentativas = 0
            codigo = False

            while tentativas < 2:
                codigo = pegar_codigo(device, velocidade_bot=velocidade_bot)
                if codigo:
                    mensagem_normal(' Código chegou: ' + str(codigo))
                    break
                else:
                    tentativas += 1

            if not codigo and tentativas == 2:
                mensagem_erro(' Código do 2nr não chegou após 2 tentativas')
                device.app_stop('pl.rs.sip.softphone.newapp')
                return 1
        else:
            mensagem_erro(
                ' O campo do código de confirmação não apareceu na tela. Possível bloqueio de IP.')
            return False

        sleep(velocidade_bot)
        # Caso apareça o codigo de confirmação, digita o codigo
        resposta = device(text='Código de confirmação').exists(timeout=30)
        if resposta:
            device(focused=True).set_text(codigo)
            mensagem_normal(' Código adicionado no input')
        else:
            mensagem_erro(' Não foi possível adicionar o código.')
            return False

        sleep(velocidade_bot)

        # Clicar em Avançar
        avançar()

        sleep(velocidade_bot)

        # Colocando a senha
        resposta = device(focused=True).exists(timeout=30)
        if resposta:
            device(focused=True).set_text(senha)
            mensagem_normal(' Senha adicionada no campo do input.')
        else:
            mensagem_erro(' Não foi possível adicionar senha')
            return False
        sleep(velocidade_bot)

        # Clicar em Avançar
        avançar()

        sleep(velocidade_bot)

        # Verificando se existe uma conta com esse número.
        resposta = device(text='CRIAR NOVA CONTA').exists(timeout=7)
        if resposta:
            device(text='CRIAR NOVA CONTA').click()
        sleep(velocidade_bot)

        # Salvar suas informações de login?
        resposta = device(
            text='Salvar suas informações de login?').exists(timeout=30)
        if resposta:
            device(text='Agora não').click()
        sleep(velocidade_bot)

        # Clicar em DEFINIR
        seletor = False
        for _ in range(30):

            if device(text='DEFINIR').exists:
                device(text='DEFINIR').click()
                seletor = True
                break

            if device(text='SET').exists:
                device(text='SET').click()
                seletor = True
                break

            sleep(1)
        if not seletor:
            mensagem_erro(' Erro ao clicar em DEFINIR/SET')
            return False

        sleep(velocidade_bot)

        # Clicar em avançar
        avançar()

        sleep(velocidade_bot)

        # Se aparecer o erro
        resposta = device(
            text='Parece que você inseriu informações incorretas. Use sua data de nascimento verdadeira.').exists(
            timeout=30)
        if resposta:
            device(text='Avançar').click()
        else:
            mensagem_erro(' Erro ao clicar em avançar')
            return False
        sleep(velocidade_bot)

        # Definindo o ano
        mensagem_normal(' Definindo idade')
        ano = randint(18, 60)
        resposta = device(
            className='android.widget.EditText').exists(timeout=30)
        if resposta:
            device(className='android.widget.EditText').set_text(str(ano))
        else:
            mensagem_erro(' Não adicionou a idade no input.')
            return False

        sleep(velocidade_bot)

        # Clicando em avançar
        avançar()

        sleep(velocidade_bot)

        # Se aparecer essa msg
        resposta = device(text='OK').exists(timeout=30)
        if resposta:
            device(text='OK').click()
        else:
            mensagem_erro(' Não clicou em OK')
            return False
        sleep(velocidade_bot)

        # Definindo o nome completo
        mensagem_normal(' Digitando o nome completo.')
        seletor = False
        for _ in range(30):

            if device(focused=True).exists:
                device(focused=True).set_text(nome)
                mensagem_normal(' Nome completo: ' + nome)
                seletor = True
                break

            if device(focused=False).exists:
                device(text='Nome completo').click()
                device(focused=True).set_text(nome)
                mensagem_normal(' Nome completo: ' + nome)
                seletor = True
                break

            sleep(1)
        if seletor == False:
            mensagem_erro(
                ' Não foi possível adicionar o nome completo no input')
            return False

        sleep(velocidade_bot)

        # Clicar em avançar
        avançar()

        sleep(velocidade_bot)

        # Definindo um nome de usuario
        resposta = device(text='Crie um nome de usuário').exists(timeout=30)
        if resposta:
            # device(className='android.widget.EditText').click()
            sleep(velocidade_bot)
            # device(className='android.widget.EditText').clear_text()
            # device(className='android.widget.EditText').set_text(usuario)
            usuario = device(className='android.widget.EditText').get_text()
            mensagem_normal(' Nome de usuário definido: ' + usuario)
        else:
            mensagem_erro(' Não foi localizado o seletor do Nome de usuário.')
            return False

        sleep(velocidade_bot)

        # Verificar se o nome de usuario existe
        if device(text=f'O nome de usuário {usuario} não está disponível.').exists(timeout=4):
            device(className='android.widget.EditText').clear_text()
            device(className='android.widget.EditText').set_text(
                usuario + '_')

            sleep(1)

        # Clicando em avançar
        avançar()

        sleep(velocidade_bot)

        # Confirmar termos de uso
        mensagem_normal(' Concordando com os termos de uso.')

        # Se apareceu isso, a conta foi criada!
        criou = False
        for x in range(60):

            # Clicando em concordo
            if device(text='Concordo').exists:
                device(text='Concordo').click()

            if device(text='Fazer uma apelação').exists:
                mensagem_desativada(' CONTA SOFREU SMS!')
                criou = False
                return 2

            if device(text='Adicione uma foto do perfil').exists:
                mensagem_sucesso(' CONTA CRIADA COM SUCESSO!')
                contador_contas += 1
                print(Fore.YELLOW + 'Quantidade criadas: ' + Style.RESET_ALL +
                      Fore.GREEN + str(contador_contas) + Style.RESET_ALL)
                criar_conta_bd(usuario, senha)
                criou = True
                return 3

            if device(text='Adicionar foto').exists:
                mensagem_sucesso(' CONTA CRIADA COM SUCESSO!')
                contador_contas += 1
                print(Fore.YELLOW + 'Quantidade criadas: ' + Style.RESET_ALL +
                      Fore.GREEN + str(contador_contas) + Style.RESET_ALL)
                criar_conta_bd(usuario, senha)
                criou = True
                return 3

            if device(text='Pular').exists:
                mensagem_sucesso(' CONTA CRIADA COM SUCESSO!')
                contador_contas += 1
                print(Fore.YELLOW + 'Quantidade criadas: ' + Style.RESET_ALL +
                      Fore.GREEN + str(contador_contas) + Style.RESET_ALL)
                create_conta_bd(usuario, senha)
                criou = True
                return 3

            sleep(1)

        if not criou:
            mensagem_desativada(
                ' Conta não foi criada! Verifique manualmente depois.')
            nao_criou(usuario, senha)
            return False

        return True
    except Exception as erro:
        print(erro)
        return False
