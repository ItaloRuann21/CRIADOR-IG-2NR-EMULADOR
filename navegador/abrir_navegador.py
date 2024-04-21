def abrir_navegador(playwright):

    try:

        # construindo navegador
        navegador = playwright.chromium.launch(
            headless=False,
            executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            args=[
                '--no-sandbox',
                '--ignore-certificate-errors',
            ]
        )

        # Criando um contexto anônimo
        contexto_anônimo = navegador.new_context()

        # Abrindo uma janela em modo anônimo
        pagina = contexto_anônimo.new_page()

        # Configurando a linguagem da página para português
        pagina.set_extra_http_headers({'Accept-Language': 'pt-br'})

        # Obtendo todas as páginas abertas (incluindo a página atual)
        todas_paginas = navegador.contexts[0].pages

        return navegador, pagina, todas_paginas

    except:
        print('erro navegador')
        return False
