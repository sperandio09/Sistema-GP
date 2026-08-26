from src.db.connection import get_connection

def listar_avaliadores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT usuario.id_usuario, usuario.nome
        FROM usuario 
        JOIN tipousuario ON usuario.id_tipousuario = tipousuario.id_tipousuario
        WHERE tipousuario.descricao = 'AVALIADOR'
    """)
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado 