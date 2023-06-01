from senha import API_KEY #pra não ter que ficar ctrl c/v na senha
import requests
import json #para a requisição

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"} #define o cabeçalho da request
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo" #a OpenAI tem diversas APIs, aqui especifico a ultima versao do chatGPT

body_mensagem = {
    "model": id_modelo, #id do modelo de API, no caso, gpt-3.5-turbo
     "messages": [{"role": "user", "content": "escreva um e-mail para o meu namorado dizendo qual a melhor constelação para ser observada em junho, no Rio de Janeiro"}] #prompt de comando
}

body_mensagem = json.dumps(body_mensagem) #pega o body da mensagem e transforma em json

requisicao = requests.post(link, headers=headers, data=body_mensagem)
#print(requisicao)
resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)
