const API_URL = "https://sistema-gp-production.up.railway.app";

async function cadastrarEscuderia(nome, turma, nome_mentor) {
  const resposta = await fetch(`${API_URL}/escuderias`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nome, turma, nome_mentor }),
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

async function obterStatusDivulgacao() {
  const resposta = await fetch(`${API_URL}/divulgacao`);
  return resposta.json();
}

async function obterDesempenhoEscuderia(idEscuderia) {
  const resposta = await fetch(
    `${API_URL}/escuderias/${idEscuderia}/desempenho`,
  );

  if (!resposta.ok) {
    throw new Error("Não foi possível carregar o desempenho da escuderia.");
  }

  return await resposta.json();
}

async function obterRanking() {
  const resposta = await fetch(`${API_URL}/ranking`);

  if (!resposta.ok) {
    throw new Error("Não foi possível carregar o ranking.");
  }

  return await resposta.json();
}

async function definirDivulgacao(
    mostrarResultado,
    dataDivulgacao
) {

    const token =
        sessionStorage.getItem(
            "admin_token"
        );


    const resposta =
        await fetch(
            `${API_URL}/divulgacao`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json",

                    "Authorization":
                        `Bearer ${token}`
                },

                body: JSON.stringify({
                    mostrar_resultado:
                        mostrarResultado,

                    data_divulgacao:
                        dataDivulgacao
                })
            }
        );


    const dados =
        await resposta.json();


    if (!resposta.ok) {

        throw new Error(
            dados.detail ||
            "Não foi possível atualizar a divulgação."
        );

    }


    return dados;
}

async function validarCodigoAdmin(codigo) {

    const resposta = await fetch(
        `${API_URL}/admin/validar`,
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                codigo: codigo
            })
        }
    );


    const dados =
        await resposta.json();


    if (!resposta.ok) {

        throw new Error(
            dados.detail ||
            "Código administrativo inválido."
        );

    }


    return dados;
}


async function verificarSessaoAdmin(token) {

    const resposta = await fetch(
        `${API_URL}/admin/verificar`,
        {
            headers: {
                "Authorization":
                    `Bearer ${token}`
            }
        }
    );


    return resposta.ok;
}

function abrirDetalhesEscuderia(idEscuderia) {

    sessionStorage.setItem(
        "id_escuderia_detalhes",
        String(idEscuderia)
    );

    const id =
        encodeURIComponent(idEscuderia);

    // Railway trabalha com URL limpa
    if (
        window.location.hostname
            .includes("railway.app")
    ) {

        window.location.href =
            `detalhesEscuderia?id=${id}`;

    } else {

        // Live Server local
        window.location.href =
            `detalhesEscuderia.html?id=${id}`;

    }
}