from src.db.connection import get_connection

def buscar_ou_criar_mentor(nome_mentor: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT usuario.id_usuario
        FROM usuario
        JOIN tipousuario ON usuario.id_tipousuario = tipousuario.id_tipousuario
        WHERE usuario.nome = %s AND tipousuario.descricao = 'MENTOR'
    """, (nome_mentor,))
    existente = cursor.fetchone()

    if existente:
        cursor.close()
        conn.close()
        return existente["id_usuario"]

    cursor.execute("SELECT id_tipousuario FROM tipousuario WHERE descricao = 'MENTOR'")
    tipo_mentor = cursor.fetchone()

    cursor.execute(
        "INSERT INTO usuario (id_tipousuario, nome) VALUES (%s, %s)",
        (tipo_mentor["id_tipousuario"], nome_mentor)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return novo_id


def criar_escuderia(nome: str, turma: str, nome_mentor: str):
    id_mentor = buscar_ou_criar_mentor(nome_mentor)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO escuderia (nome_escuderia, turma, id_mentor) VALUES (%s, %s, %s)",
        (nome, turma, id_mentor)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return novo_id

def listar_escuderias():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM escuderia')
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado