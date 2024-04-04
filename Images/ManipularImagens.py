from time import sleep

import cv2


class Imagem:
    def __init__(self, device):
        self.device = device

    def _procurar_posicao_imagem(self, template, target):
        # Converta as imagens para escala de cinza
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

        # Realize a correspondência de modelo
        result = cv2.matchTemplate(
            target_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(result)

        return result, max_loc

    def clicar_na_imagem(self, caminho_imagem: str):
        imagem_salva = cv2.imread(caminho_imagem)

        try:
            for x in range(30):
                # Captura a tela do dispositivo Android usando uiautomator2
                captura_dispositivo = self.device.screenshot(format='opencv')

                # Encontra a posição da imagem correspondente
                result, match_position = self._procurar_posicao_imagem(
                    imagem_salva, captura_dispositivo)

                # Se a confiança da correspondência for suficientemente alta
                if result[match_position[1]][match_position[0]] > 0.6:
                    # Clique na posição encontrada
                    self.device.click(match_position[0], match_position[1])
                    break
            return True
        except:
            return False

    def esperar_imagem(self, caminho_imagem: str):
        imagem_salva = cv2.imread(caminho_imagem)

        try:
            for x in range(30):
                # Captura a tela do dispositivo Android usando uiautomator2
                captura_dispositivo = self.device.screenshot(format='opencv')

                # Encontra a posição da imagem correspondente
                result, match_position = self._procurar_posicao_imagem(
                    imagem_salva, captura_dispositivo)

                # Se a confiança da correspondência for suficientemente alta
                if result[match_position[1]][match_position[0]] > 0.6:
                    # Clique na posição encontrada
                    break
            return True
        except:
            return False
