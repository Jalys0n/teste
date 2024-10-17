import sqlite3

def busca_por_login_e_senha(login, senha):
    # Concatenação direta dos valores na consulta SQL
    query = f"SELECT * FROM usuarios WHERE login = '{login}' AND senha = '{senha}'"
    
    con = sqlite3.connect('usuarios.db')
    cursor = con.cursor()
    
    try:
        # Executa a consulta diretamente com a string concatenada
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return None
    finally:
        con.close()

# Exemplo de uso inseguro
login_inserido = "' OR 1=1 --"
senha_inserida = "qualquercoisa"
usuarios = busca_por_login_e_senha(login_inserido, senha_inserida)
print(usuarios)