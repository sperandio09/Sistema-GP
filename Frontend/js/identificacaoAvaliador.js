async function carregarAvaliadores() {
    const avaliadores = await obterAvaliadores();
    const select = document.getElementById("selectAvaliador");
    avaliadores.forEach((a) => {
        const opcao = document.createElement("option");
        opcao.value = a.id_usuario;
        opcao.textContent = a.nome;
        select.appendChild(opcao);
    });
}

document.getElementById("btnConfirmar").addEventListener("click", () => {
    const select = document.getElementById("selectAvaliador");
    sessionStorage.setItem("id_avaliador", select.value);
    sessionStorage.setItem("nome_avaliador", select.options[select.selectedIndex].text);
    window.location.href = "escuderiasAvaliadas.html";
});

carregarAvaliadores();