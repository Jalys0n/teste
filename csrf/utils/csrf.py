import secrets

def generate_csrf_token():
    """
    Gera um token CSRF aleatório.
    """
    return secrets.token_hex(16)

def validate_csrf_token(session_token, received_token):
    """
    Valida o token CSRF recebido com o token da sessão.
    """
    return session_token == received_token
