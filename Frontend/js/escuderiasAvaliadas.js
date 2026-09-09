const idAvaliador = sessionStorage.getItem("id_avaliador");
if (!idAvaliador) {
    window.location.href = "validacaoAvaliador.html"
}

document.getElementById("avaliadorLogado").textContent = 
    `Avaliando como: ${sessionStorage.getItem("nome_avaliador")}`;

document.getElementById("btnBuscar").addEventListener("click", () => {
    const termo = document.getElementById("inputBusca").value.toLowerCase();
    carregarEscuderias(termo);
});

async function carregarEscuderias(termoBusca = "") {
    const escuderias = await listarEscuderias();
    const lista = document.getElementById("listaEscuderias");
    lista.innerHTML = "";

    const filtradas = escuderias.filter((e) =>
    e.nome_escuderia.toLowerCase().includes(termoBusca) ||
    e.turma.toLowerCase().includes(termoBusca)
);

filtradas.forEach((e) => {
    const item = document.createElement("li");
    item.style.cursor = "pointer"
    item.textContent = `${e.nome_escuderia} - Turma ${e.turma}`;
    item.addEventListener("click", () =>{
        window.location.href = `avaliacaoEscuderia?id=${e.id_escuderia}`;
    });
    lista.appendChild(item);
});
}
carregarEscuderias();