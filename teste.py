import requests
import time

# Sua chave de API do KoboldAI
API_KEY = "JwYLxfbojMR2LGOwBxGoBA"

# O modelo de linguagem que você deseja usar
MODEL_NAME = "KoboldAI"

# O código que você deseja gerar
PROMPT = """def greet_world():
  print("Hello, world!")

greet_world()"""

# Faça uma solicitação à API do KoboldAI para gerar código
response = requests.post(
    "https://api.koboldai.com/generate-code",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"model_name": MODEL_NAME, "prompt": PROMPT},
    timeout=5,
)

# Verifique o status da solicitação
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    generated_code = response.json()["generated_code"]

    # Execute o código gerado
    exec(generated_code)
else:
    # A solicitação falhou
    print(f"Falha ao gerar código: {response.status_code}")
