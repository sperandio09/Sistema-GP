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

def atualizar_divulgacao(mostrar_resultado: bool, data_divulgacao):
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute('SELECT id_divulgacao FROM divulgacao ORDER BY id_divulgacao DESC LIMIT 1')
     existente = cursor.fetchone()

     if existente:
          cursor.execute(
               'UPDATE divulgacao SET mostrar_resultado = %s, data_divulgacao = %s WHERE id_divulgacao = %s',
               (mostrar_resultado, data_divulgacao, existente[0])
          )
     else:
          cursor.execute(
               'INSERT INTO divulgacao (mostrar_resultado, data_divulgacao) VALUES (%s, %s)',
               (mostrar_resultado, data_divulgacao)
          )
     conn.commit()
     cursor.close()
     conn.close()

def obter_desempenho_escuderia(id_escuderia: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('''
        SELECT criterio.id_criterio, criterio.descricao, AVG(avaliacao.nota) AS media
        FROM avaliacao
        JOIN criterio ON avaliacao.id_criterio = criterio.id_criterio
        WHERE avaliacao.id_escuderia = %s
        GROUP BY criterio.id_criterio, criterio.descricao
    ''', (id_escuderia,))
    criterios = cursor.fetchall()
    for c in criterios:
        c['media'] = float(c['media'])

    cursor.execute('''
        SELECT comentario FROM avaliacao
        WHERE id_escuderia = %s AND comentario IS NOT NULL AND comentario != ''
    ''', (id_escuderia,))
    comentarios = [linha['comentario'] for linha in cursor.fetchall()]

    cursor.close()
    conn.close()

    if not criterios:
        return None 

    ranking_geral = calcular_ranking()
    posicao = None 
    nota_final = None 
    for i, item in enumerate(ranking_geral):
        if item['id_escuderia'] == id_escuderia:
            posicao = i + 1 
            nota_final = item['nota_final']
            break 
    return{
        'id_escuderia': id_escuderia,
        'posicao': posicao,
        'nota_final': nota_final,
        'criterios': criterios,
        'comentarios': comentarios
    }

