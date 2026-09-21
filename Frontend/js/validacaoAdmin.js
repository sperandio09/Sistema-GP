const CODIGO_ADMIN = "1244";

const form = document.getElementById("formValidacaoAdmin");

const inputCodigo = document.getElementById("inputCodigoAdmin");

const btnVoltar = document.getElementById("btnVoltar");

btnVoltar.addEventListener("click", () => {
  window.location.href = "paginaInicial.html";
});

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const codigoDigitado = inputCodigo.value.trim();

  if (codigoDigitado === CODIGO_ADMIN) {
   
    sessionStorage.setItem("admin_autorizado", "true");

    alert("Acesso administrativo concedido!");

    window.location.href = "admin.html";
  } else {
    alert("Código administrativo incorreto.");

    inputCodigo.value = "";

    inputCodigo.focus();
  }
});
