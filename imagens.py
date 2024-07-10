import time
import cv2


class Imagem:
    def __init__(self, device):
        self.device = device

    def procurar_posicao_imagem(self, template, target):
        # Converta as imagens para escala de cinza
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

        # Realize a correspondência de modelo
        result = cv2.matchTemplate(target_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(result)

        return result, max_loc

    def clicar_na_imagem(self, caminhos_imagens, tempo_limite=30):
        start_time = time.time()

        # Carregar todas as imagens de modelo
        imagens_salvas = [cv2.imread(caminho) for caminho in caminhos_imagens]

        while True:
            captura_dispositivo = self.device.screenshot(format='opencv')

            for imagem_salva in imagens_salvas:
                result, match_position = self.procurar_posicao_imagem(imagem_salva, captura_dispositivo)

                # Verifique se a correspondência é suficientemente boa
                if result[match_position[1], match_position[0]] > 0.6:
                    self.device.click(match_position[0], match_position[1])
                    return True

            if time.time() - start_time > tempo_limite:
                return False

    def achar_imagem(self, caminhos_imagens, tempo_limite=30):
        start_time = time.time()

        # Carregar todas as imagens de modelo
        imagens_salvas = [cv2.imread(caminho) for caminho in caminhos_imagens]

        while True:
            captura_dispositivo = self.device.screenshot(format='opencv')

            for imagem_salva in imagens_salvas:
                result, match_position = self.procurar_posicao_imagem(imagem_salva, captura_dispositivo)

                # Verifique se a correspondência é suficientemente boa
                if result[match_position[1], match_position[0]] > 0.6:
                    return True

            if time.time() - start_time > tempo_limite:
                return False


# # Exemplo de uso
# imagem = Imagem('127.0.0.1:5575')
# imagem.clicar_na_imagem(['./img/clicaInstagram.png', './img/outraImagem.png'])
