import json
import os

from mensagens.mensagens import mensagem_atencao, mensagem_sucesso


def carregar_configuracoes():
    if os.path.exists('./configuracoes.json'):
        with open('./configuracoes.json', 'r') as file:
            return json.load(file)
    return {}


def salvar_configuracoes(config):
    with open('./configuracoes.json', 'w') as file:
        json.dump(config, file, indent=4)


def configuracao():
    configuracoes_salvas = carregar_configuracoes()

    print('')
    mensagem_atencao(
        f' Digite a porta do emulador')
    porta = input('> ')
    print('')
    mensagem_atencao(
        f' Escolha o clonador: [PADRAO: {configuracoes_salvas.get("clonador", "")}]')
    clonador = input(
        f'1- Varias Contas\n2- 2accounts\n3- Aplicativo Paralelo\n> ') or configuracoes_salvas.get("clonador", "")
    print('')

    mensagem_atencao(
        f' Escolha a VPN padrão: [PADRAO: {configuracoes_salvas.get("definir_vpn", "")}]')
    definir_vpn = input(
        f'1- SurfSharke\n2- Fast VPN Freedom\n3- Super VPN Unlimited Proxy\n4- AVG VPN\n5- Criação com VPN aleatória\n> ') or configuracoes_salvas.get("definir_vpn", "")
    print('')

    mensagem_atencao(
        f' Criar quantas contas com o mesmo número? [PADRAO: {configuracoes_salvas.get("quantidade_contas_por_numero", "")}]')
    quantidade_contas_por_numero = input(
        f'> ') or configuracoes_salvas.get("quantidade_contas_por_numero", "")
    print('')
    mensagem_atencao(
        f' Gênero dos perfis: [PADRAO: {configuracoes_salvas.get("genero", "")}]')
    genero = input(
        '1- Masculino\n2- Feminina\n> ') or configuracoes_salvas.get("genero", "")
    print('')

    mensagem_atencao(
        f' Defina em segundos a velocidade do bot: [PADRAO: {configuracoes_salvas.get("velocidade_bot", "")}]')
    velocidade_bot = int(
        input('> ') or configuracoes_salvas.get("velocidade_bot", ""))
    print('')


    # Salvar configurações em um dicionário
    config = {
        "clonador": clonador,
        "definir_vpn": definir_vpn,
        "quantidade_contas_por_numero": quantidade_contas_por_numero,
        "genero": genero,
        "velocidade_bot": velocidade_bot,
    }

    # Salvar configurações em um arquivo JSON
    salvar_configuracoes(config)
    mensagem_sucesso('Configurações salvas com sucesso!')

    return porta, definir_vpn, quantidade_contas_por_numero, velocidade_bot, genero, clonador
