import lamda

def generate_poem():
    # Inicializa a LaMDA
    lamda_model = lamda.LaMDA()

    # Obtém um prompt do usuário
    prompt = input("Carro")

    # Gera o poema
    poem = lamda_model.generate_text(prompt=prompt, max_length=1000)

    # Imprime o poema
    print(poem)


if __name__ == "__main__":
    generate_poem()
