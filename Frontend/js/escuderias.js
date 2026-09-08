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

const inputBusca = document.getElementById("inputBusca");
const lista = document.getElementById("listaEscuderias");

inputBusca.addEventListener("input", () => {
    const termo = inputBusca.value.toLowerCase();
    
    if (termo.trim() === "") {
        lista.style.display = "none"; 
        lista.innerHTML = "";
    } else {
        lista.style.display = "block"; 
        carregarEscuderias(termo);
    }
});

document.getElementById("btnBuscar").addEventListener("click", () => {
    const termo = inputBusca.value.toLowerCase();
    if (termo.trim() !== "") {
        lista.style.display = "block";
        carregarEscuderias(termo);
    }
});

document.addEventListener("click", (evento) => {
    if (!inputBusca.contains(evento.target) && !lista.contains(evento.target)) {
        lista.style.display = "none";
    }
});

inputBusca.addEventListener("focus", () => {
    if (inputBusca.value.trim() !== "") {
        lista.style.display = "block";
    }
});

async function carregarEscuderias(termoBusca = "") {
    const escuderias = await listarEscuderias();
    lista.innerHTML = "";

    const filtradas = escuderias.filter((e) => 
        e.nome_escuderia.toLowerCase().includes(termoBusca) ||
        e.turma.toLowerCase().includes(termoBusca) ||
        (e.nome_mentor && e.nome_mentor.toLowerCase().includes(termoBusca))
    );

    if (filtradas.length === 0) {
        const itemVazio = document.createElement("li");
        itemVazio.textContent = "Nenhum resultado encontrado";
        itemVazio.style.color = "#999";
        lista.appendChild(itemVazio);
        return;
    }

    filtradas.forEach((e) => {
        const item = document.createElement("li");

        item.innerHTML = `<strong>${e.nome_escuderia}</strong> — Turma: ${e.turma} | Mentor: ${e.nome_mentor}`;
        
        item.addEventListener("click", () => {
            inputBusca.value = e.nome_escuderia;
            lista.style.display = "none";
        });

        lista.appendChild(item);
    });
}
