from flask import Flask, render_template, request
import random
import string

gerador_de_senha= Flask(__name__)

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

@gerador_de_senha.route('/', methods=['GET', 'POST'])
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
    gerador_de_senha.run(debug=True)
