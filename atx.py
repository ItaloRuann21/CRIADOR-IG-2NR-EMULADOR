import os
from time import sleep

from mensagens.mensagens import mensagem_atencao


def configurando_atx():
    mensagem_atencao(' Desinstalando ATX.')
    os.system('adb shell pm uninstall com.github.uiautomator')
    sleep(5)

    # Caminho para o arquivo APK
    mensagem_atencao(' Instalando ATX.')
    caminho_apk = './apks/app-uiautomator.apk'

    # Comando para instalar o APK usando adb
    comando_install = 'adb install {}'.format(caminho_apk)

    # Executar o comando de instalação usando os.system
    os.system(comando_install)

    # Aguardar um tempo para garantir que a instalação seja concluída
    sleep(5)  # Aguarda 10 segundos
