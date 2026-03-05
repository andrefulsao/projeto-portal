import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("CHAVE_PORTAL_API")
url = f"{os.getenv("API_URL")}api-de-dados/emendas"

# Configura os headers da requisição passando o token de autorização
headers = {
    "chave-api-dados": token,
    "Accept": "application/json"
}

hasNext = True
page = 1

while hasNext:
    params = {
        "pagina": page,
        "nomeAutor": "KIM KATAGUIRI"
    }

    # Faz a requisição GET
    response = requests.get(url, headers=headers, params=params)

    # Verifica o status e imprime o resultado
    if response.status_code == 200:
        print("Sucesso! Status:", response.status_code)
        try:
            data = response.json()
            if data == []:
                hasNext = False
                print("Fim da paginação")
            else:
                print("Dados:", data)
                page += 1
        except ValueError:
            print("Resposta não é um JSON válido:", response.text)
    else:
        print(f"Erro na requisição. Status: {response.status_code}")
        print("Detalhes:", response.text)