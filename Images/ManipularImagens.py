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

    def _procurar_imagem_tela(self, template_paths, target, confidence_threshold=0.6):
        target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

        for template_path in template_paths:
            # Lê a imagem em escala de cinza
            template = cv2.imread(template_path, 0)

            result = cv2.matchTemplate(
                target_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)

            if max_val > confidence_threshold:
                return True, template_path  # Retorna True e o caminho do template encontrado

        return False, None

    def esperar_imagem(self, caminho_imagem: str):
        tentativas = 0
        while tentativas < 10:
            captura_dispositivo = self.device.screenshot(format='opencv')

            res, _ = self._procurar_imagem_tela(
                [caminho_imagem], captura_dispositivo)

            if res:
                print('Imagem encontrada!')
                break
            tentativas += 1

    def clicar_na_imagem(self, caminho_imagem: str):
        imagem_salva = cv2.imread(caminho_imagem)

        try:
            tentativas = 0
            while tentativas < 10:  # Tentar até 10 vezes
                captura_dispositivo = self.device.screenshot(format='opencv')

                result, match_position = self._procurar_posicao_imagem(
                    imagem_salva, captura_dispositivo)

                if result[match_position[1]][match_position[0]] > 0.6:
                    self.device.click(match_position[0], match_position[1])
                    # Pequena pausa para permitir que o clique seja processado
                    sleep(1)
                    return True  # Retorna True se clicou com sucesso

                sleep(2)  # Aguarda 2 segundos antes de tentar novamente
                tentativas += 1

            return False  # Retorna False se não clicou após 10 tentativas
        except:
            return False
