import os
from queue import Empty, Queue  # Importar Empty corretamente
from threading import Thread
from tkinter import Label, Tk, filedialog
from tkinter.ttk import Button, Progressbar, Style

from pymongo import MongoClient

from main import main

# Variável global para controlar a execução do programa
running = True


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
            print("Login bem-sucedido!")
            os.system('cls')
            client.close()
            return True  # Login bem-sucedido, retornar True

        else:
            tentativas += 1
            print(
                f"Usuário ou senha incorretos. Tentativas restantes: {tentativas_maximas - tentativas}")

    # Se todas as tentativas falharem, retornar False
    print("Número máximo de tentativas excedido. Saindo do sistema.")
    client.close()
    return False


def get_account_count():
    try:
        # Conectar ao banco de dados MongoDB Atlas
        client = MongoClient(
            "mongodb+srv://italorvt:32578079@python-montador.exgtqsa.mongodb.net/?retryWrites=true&w=majority")
        db = client['criador-ig-2nr-privado']
        collection = db['contas_italo']

        # Contar o número de documentos na coleção
        count = collection.count_documents({})
        return count

    except Exception as e:
        print(f"Erro ao contar as contas do banco de dados: {e}")
        return 0

    finally:
        client.close()


def get_last_creation_time():
    try:
        # Conectar ao banco de dados MongoDB Atlas
        client = MongoClient(
            "mongodb+srv://italorvt:32578079@python-montador.exgtqsa.mongodb.net/?retryWrites=true&w=majority")
        db = client['criador-ig-2nr-privado']
        collection = db['contas_italo']

        # Encontrar a conta mais recente usando a data de criação
        last_creation = collection.find_one(sort=[('timestamp', -1)])
        if last_creation:
            # Formatar a data para excluir os segundos
            formatted_time = last_creation['timestamp'].strftime(
                "%d/%m/%Y %H:%M")
            return formatted_time
        else:
            return "Nenhuma conta criada ainda"

    except Exception as e:
        print(f"Erro ao obter a data da última criação: {e}")
        return "Erro ao obter data"


def baixar_contas_criadas(file_path, progress_queue):
    try:
        # Conectar ao banco de dados MongoDB Atlas
        client = MongoClient(
            "mongodb+srv://italorvt:32578079@python-montador.exgtqsa.mongodb.net/?retryWrites=true&w=majority")
        db = client['criador-ig-2nr-privado']
        collection = db['contas_italo']

        # Buscar todas as contas na coleção
        contas = list(collection.find())

        # Calcular o número total de contas
        total_contas = len(contas)
        progress_step = 100 / total_contas
        current_progress = 0

        # Abrir o arquivo TXT para escrita
        with open(file_path, mode='w', encoding='utf-8') as file:
            for index, conta in enumerate(contas, start=1):
                file.write(f"{conta['usuario']} {conta['senha']}\n")
                # Excluir a conta do banco de dados após salvá-la no arquivo
                collection.delete_one({'_id': conta['_id']})

                # Atualizar progresso
                current_progress += progress_step
                progress_queue.put(current_progress)

        # Retorna sucesso e mensagem
        return True, f"Contas salvas em {file_path}"

    except Exception as e:
        print(f"Erro ao baixar as contas do banco de dados: {e}")
        # Retorna falha e mensagem de erro
        return False, f"Erro ao baixar as contas do banco de dados: {e}"

    finally:
        client.close()


def select_file(progress_queue, result_label):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        def thread_function():
            try:
                success, message = baixar_contas_criadas(
                    file_path, progress_queue)
                result_label.config(text=message)
            except Exception as e:
                result_label.config(text=f"Erro ao baixar as contas: {e}")

        thread = Thread(target=thread_function)
        thread.start()


def create_gui():
    global running  # Indica que estamos usando a variável global 'running'

    root = Tk()
    root.title("IG CREATOR v7.1.0")

    # Definindo o tamanho fixo da janela e centralizando na tela
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width,
                  window_height, x_cordinate, y_cordinate))

    # Configurando o estilo
    style = Style()
    style.theme_use("clam")

    style.configure("TButton", background="#4863F7", foreground="white", font=("Poppins", 14), borderwidth=0,
                    focusthickness=3, focuscolor='none')
    style.map("TButton", background=[('active', '#3A4FF5')])

    root.configure(background="#363636")

    # Adicionando a quantidade de contas
    account_count = get_account_count()
    account_count_label = Label(root, text=f"Contas criadas: {account_count}", background="#363636", foreground="white",
                                font=("Poppins", 14))
    account_count_label.pack(pady=10)

    # Adicionando a data da última criação
    last_creation_time = get_last_creation_time()
    last_creation_label = Label(root, text=f"Última criação: {last_creation_time}", background="#363636",
                                foreground="white",
                                font=("Poppins", 14))
    last_creation_label.pack(pady=5)

    # Botão para baixar contas criadas
    baixar_contas_button = Button(root, text="Baixar Contas", command=lambda: select_file(progress_queue, result_label),
                                  style="TButton")
    baixar_contas_button.pack(pady=10)

    # Barra de progresso
    progress_bar = Progressbar(
        root, orient='horizontal', length=300, mode='determinate')
    progress_bar.pack(pady=10)

    # Label para exibir resultado do download
    result_label = Label(root, text="", background="#363636",
                         foreground="white", font=("Poppins", 12))
    result_label.pack(pady=5)

    def update_progress():
        while root.winfo_exists():  # Verifica se a janela ainda existe
            try:
                # Timeout para evitar bloqueio indefinido
                progress = progress_queue.get(timeout=1)
                progress_bar['value'] = progress
                root.update_idletasks()
            except Empty:
                pass  # Ignora quando a fila estiver vazia ou timeout ocorrer

    progress_queue = Queue()
    progress_thread = Thread(target=update_progress)
    progress_thread.start()

    # Configurar a função para encerrar o programa ao fechar a janela
    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    root.mainloop()


if __name__ == "__main__":
    if login():
        main()

# Para iniciar a interface de baixar contas
# if __name__ == "__main__":
#     create_gui()
