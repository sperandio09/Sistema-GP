const API_URL = "https://sistema-gp-production.up.railway.app";

async function cadastrarEscuderia(nome, turma, nome_mentor) {
    const resposta = await fetch(`${API_URL}/escuderias`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, turma, nome_mentor })
    });
    return resposta.json();
}

async function listarEscuderias() {
  const resposta = await fetch(`${API_URL}/escuderias`);
  return resposta.json();
}

async function obterCriterios() {
  const resposta = await fetch(`${API_URL}/criterios`);
  return resposta.json();
}

async function obterAvaliadores() {
  const resposta = await fetch(`${API_URL}/avaliadores`);
  return resposta.json();
}

async function cadastrarAvaliacao(
  id_escuderia,
  id_avaliador,
  id_criterio,
  nota,
  comentario,
) {
  const resposta = await fetch(`${API_URL}/avaliacoes`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id_escuderia,
      id_avaliador,
      id_criterio,
      nota,
      comentario,
    }),
  });
  return resposta.json();
}
