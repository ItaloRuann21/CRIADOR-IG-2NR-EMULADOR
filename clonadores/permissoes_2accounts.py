def aceitando_permissoes_2accounts(device):
    """Concede as permissões necessárias ao aplicativo de destino (com.excelliance.multiaccount).

    Registra as permissões concedidas usando o objeto logger.

    Levanta:
        OSError: Se ocorrer um erro durante a execução do comando shell.
    """

    # Permissões necessárias para acesso a arquivos e mídia, contatos, câmera, otimização de bateria e sobrepor outros apps
    permissoes = [
        # Ler arquivos e mídia no dispositivo
        "android.permission.READ_EXTERNAL_STORAGE",
        # Escrever arquivos e mídia no dispositivo
        "android.permission.WRITE_EXTERNAL_STORAGE",
        "android.permission.READ_CONTACTS",         # Ler dados de contato
        "android.permission.WRITE_CONTACTS",        # Escrever dados de contato
        "android.permission.CALL_PHONE",  # Permissão para fazer chamadas telefônicas
    ]

    for permissao in permissoes:

        device.shell(
            ['pm', 'grant', "com.excelliance.multiaccount", permissao])
