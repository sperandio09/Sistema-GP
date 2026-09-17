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
    cursor.execute('''
    SELECT escuderia.id_escuderia, escuderia.nome_escuderia, escuderia.turma, usuario.nome AS nome_mentor 
    FROM escuderia 
    JOIN usuario ON escuderia.id_mentor = usuario.id_usuario
    ''')
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultado

def listar_escuderias_avaliadas(id_avaliador: int):

    conn = get_connection()
    cursor  = conn.cursor(dictionary=True)

    query = """
        SELECT
            e.id_escuderia,
            e.nome_escuderia,
            e.turma,
            u.nome AS mentor,

            COUNT(DISTINCT a.id_criterio) AS criterios_avaliados,

            (SELECT COUNT(*) FROM criterio) AS total_criterios,

            CASE
                WHEN COUNT(DISTINCT a.id_criterio) =
                     (SELECT COUNT(*) FROM criterio)
                THEN 'concluida'
                ELSE 'em_andamento'
            END AS status

        FROM avaliacao a

        INNER JOIN escuderia e
            ON e.id_escuderia = a.id_escuderia

        LEFT JOIN usuario u
            ON u.id_usuario = e.id_mentor

        WHERE a.id_avaliador = %s

        GROUP BY
            e.id_escuderia,
            e.nome_escuderia,
            e.turma,
            u.nome

        ORDER BY e.nome_escuderia
    """

    cursor.execute(query, (id_avaliador,))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultados
