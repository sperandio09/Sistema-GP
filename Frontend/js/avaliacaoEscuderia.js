//const idAvaliador = sessionStorage.getItem("id_avaliador");
//if (!idAvaliador){
//    window.location.href = "validacaoAvaliador.html";    
//}

const parametros = new URLSearchParams(window.location.search);
const idEscuderia = parametros.get("id");

async function montarFormulario() {
    const criterios = await obterCriterios();
    const form = document.getElementById("formAvaliacao");
    
    criterios.forEach((c) => {
        const bloco = document.createElement("div");
        bloco.classList.add("bloco-criterio");
        bloco.innerHTML = `
        <strong>${c.descricao}</strong>
        <br>
        <label>Nota (0 a 10): <input type="number" min="0" max="10" step="0.5" id="nota_${c.id_criterio}" required></label>
        <br>
        <textarea id="comentario_${c.id_criterio}" placeholder="Comentário (opcional)" style="width: 100%; margin-top: 5px;"></textarea>
        `;
        form.appendChild(bloco);
    });
}

document.getElementById("btnEnviar").addEventListener("click", async () => {
    const criterios = await obterCriterios();

    for (const c of criterios){
        const nota = document.getElementById(`nota_${c.id_criterio}`).value;
        const comentario = document.getElementById(`comentario_${c.id_criterio}`).value;

        const resultado = await cadastrarAvaliacao(idEscuderia, idAvaliador, c.id_criterio, parseFloat(nota), comentario);
        if (resultado.detail) {
            alert(`Erro no critério "${c.descricao}": ${resultado.detail}`)
            return;
        }
    }
    alert("Avaliação enviada com sucesso!");
    window.location.href = "escuderiasAvaliadas.html";
});

montarFormulario();