import cv2
import numpy as np

# Conecte-se à câmera indexada como 0
camera = cv2.VideoCapture(0)

# Defina a largura e altura do quadro como 640 x 480
camera.set(3, 640)
camera.set(4, 480)

# Carregue a imagem da montanha
mountain = cv2.imread('mount_everest.jpg')

# Redimensione a imagem da montanha para 640 x 480
mountain = cv2.resize(mountain, (640, 480))

while True:
    # Leia um quadro da câmera conectada
    status, frame = camera.read()

    # Se o quadro foi obtido com sucesso
    if status:
        # Inverta o quadro
        frame = cv2.flip(frame, 1)

        # Converta a imagem para RGB para facilitar o processamento
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Crie os limites
        lower_bound = np.array([100, 100, 100])
        upper_bound = np.array([255, 255, 255])

        # Máscara da imagem dentro dos limites
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # Inverta a máscara
        mask = cv2.bitwise_not(mask)

        # Extraia o primeiro plano/pessoa usando bitwise_and
        foreground = cv2.bitwise_and(frame, frame, mask=mask)

        # Crie a imagem final
        final_image = cv2.addWeighted(foreground, 1, mountain, 0.5, 0)

        # Exiba a imagem final
        cv2.imshow('Quadro', final_image)

        # Aguarde 1 ms antes de exibir o próximo quadro
        code = cv2.waitKey(1)
        if code == 32:  # Pressione a tecla espaço para sair
            break

# Libere a câmera e feche todas as janelas
camera.release()
cv2.destroyAllWindows()
