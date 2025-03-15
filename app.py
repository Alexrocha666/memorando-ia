from flask import Flask, request, jsonify
import openai  # Instale com `pip install openai`
import os

app = Flask(__name__)

openai.api_key = "> Running 'gunicorn -w 4 app:app'
[2025-03-15 02:11:22 +0000] [92] [INFO] Starting gunicorn 23.0.0
[2025-03-15 02:11:22 +0000] [92] [INFO] Listening at: http://0.0.0.0:10000 (92)
[2025-03-15 02:11:22 +0000] [92] [INFO] Using worker: sync
[2025-03-15 02:11:22 +0000] [93] [INFO] Booting worker with pid: 93
[2025-03-15 02:11:22 +0000] [94] [INFO] Booting worker with pid: 94
[2025-03-15 02:11:22 +0000] [95] [INFO] Booting worker with pid: 95
[2025-03-15 02:11:22 +0000] [96] [INFO] Booting worker with pid: 96
127.0.0.1 - - [15/Mar/2025:02:11:23 +0000] "HEAD / HTTP/1.1" 404 0 "-" "Go-http-client/1.1"
==> Your service is live 🎉
127.0.0.1 - - [15/Mar/2025:02:11:29 +0000] "GET / HTTP/1.1" 404 207 "-" "Go-http-client/2.0"
127.0.0.1 - - [15/Mar/2025:02:12:28 +0000] "GET / HTTP/1.1" 404 207 "-" "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36""  # Substitua pela sua chave da OpenAI

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
