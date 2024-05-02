import os

from pymongo import MongoClient

from main import main
from mensagens.mensagens import mensagem_erro, mensagem_sucesso


def login():
    # Conectar ao banco de dados MongoDB Atlas
    client = MongoClient(
        "mongodb+srv://italorvt:32578079@python-montador.exgtqsa.mongodb.net/?retryWrites=true&w=majority")
    # Modifique para o nome do seu banco de dados
    db = client['criador-ig-2nr-privado']
    # Modifique para o nome da sua coleção
    collection = db['pessoas']

    tentativas_maximas = 3
    tentativas = 0

    while tentativas < tentativas_maximas:
        usuario = input('Usuário: ')
        senha = input('Senha: ')

        # Verificar se o usuário e a senha correspondem aos registros no banco de dados
        user_data = collection.find_one({'usuario': usuario, 'senha': senha})

        if user_data:
            mensagem_sucesso(" Login bem-sucedido!")
            os.system('cls')
            client.close()
            return True  # Login bem-sucedido, retornar True

        else:
            tentativas += 1
            mensagem_erro(" Usuário ou senha incorretos. Tentativas restantes: {}".format(
                tentativas_maximas - tentativas))

    # Se todas as tentativas falharem, retornar False
    mensagem_erro(" Número máximo de tentativas excedido. Saindo do sistema.")
    client.close()
    return False


if __name__ == "__main__":
    if login():
        main()
