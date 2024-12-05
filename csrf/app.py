from flask import Flask, render_template, request, session
from utils.csrf import generate_csrf_token, validate_csrf_token
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Chave secreta para sessões

@app.route('/form', methods=['GET'])
def form():
    # Gera e armazena o token CSRF
    csrf_token = generate_csrf_token()
    session['csrf_token'] = csrf_token
    return render_template('form.html', csrf_token=csrf_token)

@app.route('/alterar-email', methods=['POST'])
def alterar_email():
    # Exibe tokens para debug
    print("Token armazenado na sessão:", session.get('csrf_token'))
    print("Token enviado no formulário:", request.form.get('csrf_token'))
    
    # Valida o token CSRF
    if not validate_csrf_token(session.get('csrf_token'), request.form.get('csrf_token')):
        return "Token CSRF inválido!", 403

    # Lógica para alterar o e-mail
    novo_email = request.form.get('novo_email')
    return f"E-mail alterado para: {novo_email}!"

@app.route('/ataque', methods=['GET'])
def ataque():
    return render_template('ataque.html')

if __name__ == '__main__':
    app.run(debug=True)
