import sqlite3

def busca_por_login_e_senha(login, senha):
    # Usando placeholders (parâmetros) para evitar SQL Injection
    query = "SELECT * FROM usuarios WHERE login = ? AND senha = ?"
    
    con = sqlite3.connect('usuarios.db')
    cursor = con.cursor()
    
    try:
        # Usa parâmetros ao invés de concatenar a string
        cursor.execute(query, (login, senha))
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return None
    finally:
        con.close()

# Exemplo de uso seguro
login_inserido = "' OR 1=1 --"
senha_inserida = "qualquercoisa"
usuarios = busca_por_login_e_senha(login_inserido, senha_inserida)
print(usuarios)
