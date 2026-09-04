document.getElementById("formCadastroEscuderia").addEventListener("submit", async (evento) => {
  evento.preventDefault();
  
  const nomeEscuderia = document.getElementById("inputNomeEscuderia").value;
  const turma = document.getElementById("inputTurma").value;
  const nomeMentor = document.getElementById("inputMentor").value.toUpperCase();

  const resultado = await cadastrarEscuderia(nomeEscuderia, turma, nomeMentor);
  alert(resultado.mensagem || "Escuderia cadastrada com sucesso!");
  document.getElementById("formCadastroEscuderia").reset();
  carregarEscuderias();
});

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
        item.textContent = `Escuderia: ${e.nome_escuderia}, Turma: ${e.turma}, Mentor: ${e.nome_mentor}`;
        lista.appendChild(item);
    });
} 

carregarEscuderias();