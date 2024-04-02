def aceitando_permissoes_2nr(device):
    """Concede as permissões necessárias ao aplicativo de destino (com.excelliance.multiaccount).

    Registra as permissões concedidas usando o objeto logger.

    Levanta:
        OSError: Se ocorrer um erro durante a execução do comando shell.
    """

    # Permissões necessárias para acesso a arquivos e mídia, contatos, câmera, otimização de bateria e sobrepor outros apps
    permissoes = [
        "android.permission.READ_EXTERNAL_STORAGE",     # Ler arquivos e mídia no dispositivo
        "android.permission.WRITE_EXTERNAL_STORAGE",    # Escrever arquivos e mídia no dispositivo
        "android.permission.READ_CONTACTS",            # Ler dados de contato
        "android.permission.WRITE_CONTACTS",           # Escrever dados de contato
        "android.permission.CAMERA",                   # Acessar a câmera do dispositivo
        "android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS",  # Ignorar otimizações de bateria
        "android.permission.SYSTEM_ALERT_WINDOW",      # Sobrepor outros aplicativos
        "android.permission.RECORD_AUDIO",             # Gravar áudio (microfone)
    ]

    for permissao in permissoes:
        device.shell(['pm', 'grant', "pl.rs.sip.softphone.newapp", permissao])