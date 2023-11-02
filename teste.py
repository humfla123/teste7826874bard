import requests

# Sua chave de API do KoboldAI
API_KEY = "JwYLxfbojMR2LGOwBxGoBA"

# O modelo de linguagem que você deseja usar
MODEL_NAME = "KoboldAI"

# O texto que você deseja gerar
PROMPT = "Escreva um poema sobre um gato."

# Faça uma solicitação à API do KoboldAI para gerar texto
response = requests.post(
    "https://api.koboldai.com/generate-text",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"model_name": MODEL_NAME, "prompt": PROMPT},
)

# Verifique o status da solicitação
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    generated_text = response.json()["generated_text"]

    # Imprima o texto gerado
    print(generated_text)
else:
    # A solicitação falhou
    print("Falha ao gerar texto:", response.status_code)
