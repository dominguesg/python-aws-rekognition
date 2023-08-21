import requests
import os

# Configurações da API do Pexels
PEXELS_API_KEY = "B8GBp2R6M3rM6ivhGsRnYa9PqUEhTu0N8iHwWsNWyKg7NF0JtyVY2Cti"
PEXELS_COLLECTION_ID = "rwhhf6c"

# Pasta de destino para salvar as imagens localmente
LOCAL_SAVE_FOLDER = "pexels_images"

# Criar a pasta se ela não existir
if not os.path.exists(LOCAL_SAVE_FOLDER):
    os.makedirs(LOCAL_SAVE_FOLDER)

# URL da API do Pexels para obter imagens da coleção
PEXELS_COLLECTION_URL = f"https://api.pexels.com/v1/collections/{PEXELS_COLLECTION_ID}"

# Definir os cabeçalhos da solicitação
headers = {
    "Authorization": f"{PEXELS_API_KEY}"
}

# Fazer a solicitação para a API do Pexels
response = requests.get(PEXELS_COLLECTION_URL, headers=headers)
collection_data = response.json().get("media", []) if response.status_code == 200 else []

# Baixar as imagens e salvar localmente
for item in collection_data:
    image_url = item.get("src").get("original")
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        
        image_filename = os.path.basename(image_url)
        local_save_path = os.path.join(LOCAL_SAVE_FOLDER, image_filename)
        
        with open(local_save_path, "wb") as f:
            f.write(image_data)
        
        print(f"Imagem {image_filename} salva localmente.")
    else:
        print(f"Falha ao baixar imagem {image_url}.")

print("Processo concluído.")
