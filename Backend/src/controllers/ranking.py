from src.db.connection import get_connection

def obter_status_divulgacao():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT mostrar_resultado, data_divulgacao FROM divulgacao ORDER BY id_divulgacao DESC LIMIT 1')
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return resultado 

def calcular_ranking():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT escuderia.id_escuderia, escuderia.nome_escuderia, avaliacao.id_criterio, AVG(avaliacao.nota) AS media_criterio
        FROM avaliacao
        JOIN escuderia ON avaliacao.id_escuderia = escuderia.id_escuderia
        GROUP BY escuderia.id_escuderia, escuderia.nome_escuderia, avaliacao.id_criterio
    ''')
    linhas = cursor.fetchall()
    cursor.close()
    conn.close()

    escuderias = {}
    for linha in linhas:
        id_esc = linha['id_escuderia']
        if id_esc not in escuderias:
                escuderias[id_esc] = {
                    'id_escuderia': id_esc,
                    'nome_escuderia': linha['nome_escuderia'],
                    'medias_criterios': []
        }
    escuderias[id_esc]['medias_criterios'].append(float(linha['media_criterio']))

    ranking = []
    for escuderia in escuderias.values():
        medias = escuderia['medias_criterios']
        nota_final = sum(medias) / len(medias)
        ranking.append({
        'id_escuderia': escuderia['id_escuderia'],
        'nome_escuderia': escuderia['nome_escuderia'],
        'nota_final': round(nota_final, 2)
    })

    ranking.sort(key=lambda x: x['nota_final'], reverse=True)
    return ranking

