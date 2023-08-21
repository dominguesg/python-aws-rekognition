import os
import cv2
import numpy as np
from skimage import exposure
from skimage import img_as_ubyte
from skimage import io


def load_and_preprocess_image(image_path, target_size=(224, 224)):
    image = io.imread(image_path)

    # Redimensionar a imagem para o tamanho alvo
    # image = cv2.resize(image, target_size)

    # Normalização das intensidades de pixel para o intervalo [0, 1]
    image = image / 255.0

    return image


def augment_image(image):
    # Aplicar data augmentation, por exemplo, rotação aleatória e espelhamento horizontal
    if np.random.rand() < 0.5:
        image = np.fliplr(image)
    angle = np.random.randint(-10, 10)
    image = img_as_ubyte(exposure.adjust_gamma(image, gamma=1.2))
    image = img_as_ubyte(exposure.adjust_log(image, gain=1, inv=False))
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    image = cv2.warpAffine(image, M, (cols, rows))

    return image


# Diretório contendo as imagens originais
input_directory = "images"

# Diretório onde as imagens pré-processadas e aumentadas serão salvas
output_directory = "processed-images"

# Garantir que o diretório de saída exista
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Processar e salvar as imagens
for filename in os.listdir(input_directory):
    if (
        filename.endswith(".jpg")
        or filename.endswith(".png")
        or filename.endswith(".jpeg")
        or filename.endswith(".JPEG")
    ):
        print(f"Processando o arquivo {filename} ...")
        image_path = os.path.join(input_directory, filename)
        image = load_and_preprocess_image(image_path)

        # Salvar a imagem pré-processada
        print(f"Salvando o arquivo  {filename} processado!")
        filename_split = os.path.splitext(filename)
        name_original = filename_split[0]
        extension = filename_split[1]
        output_path = os.path.join(
            output_directory, f"{name_original}_processed{extension}"
        )
        cv2.imwrite(output_path, image * 255.0)

        print("Aplicando Data Augmentation...")
        # Aplicar data augmentation e salvar versões aumentadas
        range = range(5)
        for i in range:
            print(f"Data Augmentation {i} de {range.}")
            augmented_image = augment_image(image)
            augmented_filename = f"{name_original}_augmented_{i+1}{extension}"
            augmented_output_path = os.path.join(output_directory, augmented_filename)
            print(f"Salvando arquivo de Data Augmentation {i} de {range.count}")
            cv2.imwrite(augmented_output_path, augmented_image)

print("Pré-processamento e aumento de dados concluídos.")
