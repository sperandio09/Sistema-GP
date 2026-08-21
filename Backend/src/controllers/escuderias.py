from src.db.connection import get_connection 

def criar_escuderia(nome_escuderia: str, turma: str, id_mentor: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO escuderia (nome_escuderia, turma, id_mentor) VALUES (%s, %s, %s)', (nome_escuderia, turma, id_mentor))
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