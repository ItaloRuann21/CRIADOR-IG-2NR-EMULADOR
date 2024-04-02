def contas_criadas(usuario, senha):
    with open('contas_criadas.txt', 'a+', encoding='utf8') as arquivo_ativas:
            arquivo_ativas.write(f'{usuario} {senha}\n')

def nao_criou(usuario, senha):
    with open('nao_criou.txt', 'a+', encoding='utf8') as arquivo_ativas:
            arquivo_ativas.write(f'{usuario} {senha}\n')

def contas_2nr(email, senha):
    with open('2nr_contas.txt', 'a+', encoding='utf8') as arquivo_ativas:
            arquivo_ativas.write(f'{email} {senha}\n')

def verificar_se_criou(email, senha):
    with open('verificar_se_criou.txt', 'a+', encoding='utf8') as arquivo_ativas:
            arquivo_ativas.write(f'{email} {senha}\n')