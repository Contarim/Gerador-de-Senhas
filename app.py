from flask import Flask, request, render_template
import random
import string
import os

app = Flask(__name__)

# Configurações para ambiente de produção
app.config['ENV'] = 'production'

# Função para gerar a senha
def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits

    simbolos_permitidos = "!@#$%&*-+?/\\"  # Símbolos permitidos

    if usar_simbolos:
        caracteres += simbolos_permitidos

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

@app.route('/', methods=['GET', 'POST'])
def index():
    senha = None
    tamanho = 12
    usar_maiusculas = True
    usar_numeros = True
    usar_simbolos = True

    if request.method == 'POST':
        tamanho = int(request.form.get('tamanho', 12))
        usar_maiusculas = 'maiusculas' in request.form
        usar_numeros = 'numeros' in request.form
        usar_simbolos = 'simbolos' in request.form

        senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)

    return render_template(
        'index.html',
        senha=senha,
        tamanho=tamanho,
        usar_maiusculas=usar_maiusculas,
        usar_numeros=usar_numeros,
        usar_simbolos=usar_simbolos
    )

# Endpoint para manter a aplicação ativa
@app.route('/heartbeat')
def heartbeat():
    return 'OK', 200  # Responde com "OK" para indicar que o servidor está ativo

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
