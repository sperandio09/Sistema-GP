from src.db.connection import get_connection

def listar_criterios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM criterio')
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado 