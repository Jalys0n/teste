import secrets

def generate_csrf_token():
    """Gera um token CSRF único."""
    return secrets.token_hex(16)

def validate_csrf_token(session_token, form_token):
    """Valida o token CSRF enviado no formulário."""
    return session_token == form_token
