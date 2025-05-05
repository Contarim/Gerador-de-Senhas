import Flask
import random
import string
import os

app = Flask(__name__)

# Configurações para ambiente de produção
app.config['ENV'] = 'production'

# Função para gerar a senha
def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    # Caracteres básicos
    caracteres = string.ascii_lowercase
    
    # Adicionar letras maiúsculas, números e símbolos com base nas opções
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits

    # Definir a lista de símbolos personalizados
    simbolos_permitidos = "!@#$%&*-+?\/"
    
    if usar_simbolos:
        caracteres += simbolos_permitidos  # Apenas os símbolos definidos na variável

    # Gerar a senha
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

@app.route('/', methods=['GET', 'POST'])
def index():
    senha = None
    if request.method == 'POST':
        # Obter os valores do formulário
        tamanho = int(request.form.get('tamanho', 12))
        usar_maiusculas = 'maiusculas' in request.form
        usar_numeros = 'numeros' in request.form
        usar_simbolos = 'simbolos' in request.form
        
        # Gerar a senha com as opções fornecidas
        senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)

    return render_template('index.html', senha=senha)

if __name__ == '__main__':
    # Certifique-se de que o Flask escute na porta correta no Render
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
