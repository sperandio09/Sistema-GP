from src.db.connection import get_connection
import mysql.connector

def criar_avaliacao(id_escuderia: int, id_avaliador: int, id_criterio: int, nota: float, comentario: str | None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO avaliacao (id_escuderia, id_avaliador, id_criterio, nota, comentario) VALUES (%s, %s, %s, %s, %s)",
            (id_escuderia, id_avaliador, id_criterio, nota, comentario)
        )
        conn.commit()
        novo_id = cursor.lastrowid
        return novo_id
    except mysql.connector.errors.IntegrityError:
        raise ValueError ('Este avaliador já avaliou esse critério para essa escuderia.')
    finally:
        cursor.close()
        conn.close()
            