import requests
import os

# Configurações da API do Unsplash
UNSPLASH_ACCESS_KEY = "j9d2ohCxjZqZjzHJUqRQIImpTh67-Y656bSeROKPxLE"
UNSPLASH_COLLECTION_ID = "eqnJ4KeXzYM"

# Pasta de destino para salvar as imagens localmente
LOCAL_SAVE_FOLDER = "images"

# Criar a pasta se ela não existir
if not os.path.exists(LOCAL_SAVE_FOLDER):
    os.makedirs(LOCAL_SAVE_FOLDER)

# URL da API do Unsplash para obter imagens da coleção
UNSPLASH_COLLECTION_URL = f"https://api.unsplash.com/collections/{UNSPLASH_COLLECTION_ID}/photos"

# Definir os parâmetros da solicitação
params = {
    "client_id": UNSPLASH_ACCESS_KEY,
    "per_page": 30  # Número de imagens a serem obtidas
}

# Fazer a solicitação para a API do Unsplash
response = requests.get(UNSPLASH_COLLECTION_URL, params=params)
collection_data = response.json() if response.status_code == 200 else []

# Baixar as imagens e salvar localmente
for item in collection_data:
    image_url = item.get("urls").get("raw")
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        
        image_filename = item.get("slug") + ".jpeg"
        local_save_path = os.path.join(LOCAL_SAVE_FOLDER, image_filename)
        
        with open(local_save_path, "wb") as f:
            f.write(image_data)
        
        print(f"Imagem {image_filename} salva localmente.")
    else:
        print(f"Falha ao baixar imagem {image_url}.")

print("Processo concluído.")
