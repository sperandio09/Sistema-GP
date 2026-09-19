from src.db.connection import get_connection
import mysql.connector


def criar_avaliacao(
    id_escuderia: int,
    id_avaliador: int,
    id_criterio: int,
    nota: float,
    comentario: str | None
):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:

        # Verifica se os resultados estão divulgados
        cursor.execute("""
            SELECT mostrar_resultado
            FROM divulgacao
            ORDER BY id_divulgacao DESC
            LIMIT 1
        """)

        divulgacao = cursor.fetchone()

        if divulgacao and divulgacao["mostrar_resultado"]:

            raise PermissionError(
                "As avaliações estão encerradas enquanto "
                "os resultados estiverem divulgados."
            )


        # Cadastra a avaliação
        cursor.execute("""
            INSERT INTO avaliacao
            (
                id_escuderia,
                id_avaliador,
                id_criterio,
                nota,
                comentario
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            id_escuderia,
            id_avaliador,
            id_criterio,
            nota,
            comentario
        ))

        conn.commit()

        return cursor.lastrowid


    except mysql.connector.errors.IntegrityError as erro:

        conn.rollback()

        if erro.errno == 1062:

            raise ValueError(
                "Este avaliador já avaliou esse critério "
                "para essa escuderia."
            )

        raise


    except PermissionError:

        conn.rollback()
        raise


    except Exception:

        conn.rollback()
        raise


    finally:

        cursor.close()
        conn.close()