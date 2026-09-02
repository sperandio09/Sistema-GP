const API_URL = "https://sistema-gp-production.up.railway.app";

async function cadastrarEscuderia(nome, turma, id_mentor){
    const resposta = await fetch(`${API_URL}/escuderias`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, turma, id_mentor })
    });
    return resposta.json();
}

async function listarEscuderias(){
    const resposta = await fetch(`${API_URL}/escuderias`);
    return resposta.json();
}
