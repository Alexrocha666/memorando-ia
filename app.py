from flask import Flask, request, jsonify
import openai  # Instale com `pip install openai`
import os

app = Flask(__name__)

# Recuperando a chave de API de uma variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")  # A chave da OpenAI deve ser configurada como variável de ambiente

@app.route('/')
def home():
    return 'Página inicial funcionando!'

@app.route("/gerar", methods=["POST"])
def gerar_memorando():
    dados = request.json
    prompt = f"Crie um memorando formal para {dados['destinatario']} com o assunto '{dados['assunto']}'"

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    memorando = resposta["choices"][0]["message"]["content"]
    return jsonify({"memorando": memorando})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Obtém a porta configurada no Render
    app.run(host="0.0.0.0", port=port, debug=True)  # Aceita conexões externas
