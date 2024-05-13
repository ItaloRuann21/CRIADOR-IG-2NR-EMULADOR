import os
from time import sleep

from mensagens.mensagens import mensagem_atencao


def configurando_atx():
    mensagem_atencao(' Desinstalando ATX.')
    os.system('adb shell pm uninstall com.github.uiautomator')
    sleep(2)
    os.system('adb shell pm uninstall com.github.uiautomator.test')
    sleep(5)

    # Caminho para o arquivo APK
    mensagem_atencao(' Instalando ATX.')
    caminho_apk = './apks/app-uiautomator.apk'
    caminho_apk_test = './apks/app-uiautomator-test.apk'

    # Comando para instalar o APK usando adb
    comando_install = 'adb install {}'.format(caminho_apk)
    comando_install_test = 'adb install {}'.format(caminho_apk_test)

    # Executar o comando de instalação usando os.system
    os.system(comando_install)
    sleep(3)
    os.system(comando_install_test)

    # Aguardar um tempo para garantir que a instalação seja concluída
    sleep(5)  # Aguarda 10 segundos
