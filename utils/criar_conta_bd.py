from pymongo import MongoClient
from datetime import datetime


def create_conta_bd(usuario, senha):
    try:
        # Conectar ao banco de dados MongoDB Atlas
        client = MongoClient(
            "mongodb+srv://italorvt:32578079@python-montador.exgtqsa.mongodb.net/?retryWrites=true&w=majority")
        db = client['criador-ig-2nr-privado']
        collection = db['contas_italo']

        # Inserir nova conta no banco de dados
        conta = {
            'usuario': usuario,
            'senha': senha,
            'timestamp': datetime.now()
        }
        collection.insert_one(conta)
        return True

    except Exception as e:
        print(f"Erro ao criar conta no banco de dados: {e}")
        return False

    finally:
        client.close()