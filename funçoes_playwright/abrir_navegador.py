def abrir_navegador(playwright):

    try:

        # construtor do navegador
        navegador = playwright.chromium.launch(
            headless=False, executable_path='C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
            args=[
                '--no-sandbox',
                '--ignore-certificate-errors',
            ]
        )

        # Criando um contexto anônimo
        contexto_anônimo = navegador.new_context()

        # Abrindo uma janela em modo anônimo
        pagina = contexto_anônimo.new_page()

        # Definindo o tamanho da tela
        pagina.set_viewport_size({"width": 800, "height": 600})

        # Configurando a linguagem da página para português
        pagina.set_extra_http_headers({'Accept-Language': 'pt-br'})

        return navegador, pagina

    except Exception as error:
        print(error)
        return False
