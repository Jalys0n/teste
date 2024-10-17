import sqlite3

# Cria uma conexão com o banco de dados (ou cria um novo arquivo de banco de dados)
con = sqlite3.connect('usuarios.db')

# Cria um cursor para executar comandos SQL
cursor = con.cursor()

# Cria a tabela 'usuarios' no banco de dados, se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# Insere alguns dados de teste na tabela 'usuarios'
cursor.executemany('''
INSERT INTO usuarios (login, senha) VALUES (?, ?)
''', [
    ('admin', '123456'),
    ('user1', 'password'),
    ('user2', 'senha123'),
])

# Confirma as alterações no banco de dados
con.commit()

# Consulta os dados para verificar se foram inseridos corretamente
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

# Fecha a conexão com o banco de dados
con.close()

print (resultados)
