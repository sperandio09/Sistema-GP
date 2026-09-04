const CODIGO_VALIDACAO = "2696";

const form = document.getElementById("formValidacao");
const inputCodigo = document.getElementById("inputCodigo");
const btnVoltar = document.getElementById("btnVoltar");

btnVoltar.addEventListener("click", () => {
  window.location.href = "paginaInicial.html";
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const codigoDigitado = inputCodigo.value;

  if (codigoDigitado === CODIGO_VALIDACAO) {
    alert("Acesso concedido! Redirecionando para a página de avaliação...");
    window.location.href = "avaliacao.html";
  } else {
    alert("Código de validação incorreto. Tente novamente.");
    inputCodigo.value = "";
    inputCodigo.focus();
  }
});
