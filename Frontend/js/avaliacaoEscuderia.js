const idAvaliador = sessionStorage.getItem("id_avaliador");

if (!idAvaliador) {
    window.location.href = "validacaoAvaliador.html";
}

const parametros = new URLSearchParams(window.location.search);
const idEscuderia = parametros.get("id");


function obterComentarioPadrao(idCriterio, nota) {

    nota = Number(nota);

    const comentarios = {

        // CRITÉRIO 9
        // Apresentação do Elevator Pitch
        9: {
            nota10:
                "A equipe apresentou uma excelente postura, vendendo a ideia de forma convincente.",

            nota6a9:
                "A equipe apresentou com uma boa postura e vendendo bem a ideia.",

            nota1a5:
                "A equipe apresentou razoavelmente, vendendo pouco a ideia.",

            nota0:
                "A equipe não apresentou."
        },


        // CRITÉRIO 10
        // Caráter inovador e potencial de mercado
        10: {
            nota10:
                "O Pitch reforçou de forma excelente o caráter inovador e o potencial de mercado do projeto perante possíveis concorrentes.",

            nota6a9:
                "O Pitch reforçou bem o caráter inovador e o potencial de mercado do projeto perante possíveis concorrentes.",

            nota1a5:
                "O Pitch reforçou pouco o caráter inovador e o potencial de mercado do projeto perante possíveis concorrentes.",

            nota0:
                "O Pitch não apresentou essas informações."
        },


        // CRITÉRIO 11
        // Abrangência do Projeto
        11: {
            nota10:
                "A inovação do projeto possui abrangência mundial.",

            nota6a9:
                "A inovação do projeto possui abrangência nacional.",

            nota1a5:
                "A inovação do projeto possui abrangência regional.",

            nota0:
                "O projeto não é inovador."
        },


        // CRITÉRIO 12
        // Grau de Inovação do Projeto
        12: {
            nota10:
                "As características/funcionalidades do projeto inovador não possuem soluções similares no mercado ou apresentam elevado grau de diferenciação.",

            nota6a9:
                "As características/funcionalidades do projeto inovador apresentam intermediário grau de diferenciação em relação às soluções existentes no mercado.",

            nota1a5:
                "As características/funcionalidades do projeto inovador apresentam baixo grau de diferenciação em relação às soluções existentes no mercado.",

            nota0:
                "O projeto não apresenta essas informações."
        }

    };


    const criterio = comentarios[idCriterio];

    if (!criterio) {
        return "";
    }


    // NOTA 10
    if (nota === 10) {
        return criterio.nota10;
    }


    // NOTAS DE 6 ATÉ ABAIXO DE 10
    if (nota >= 6 && nota < 10) {
        return criterio.nota6a9;
    }


    // NOTAS DE 1 ATÉ ABAIXO DE 6
    if (nota >= 1 && nota < 6) {
        return criterio.nota1a5;
    }


    // NOTA ZERO
    if (nota === 0) {
        return criterio.nota0;
    }


    return "";
}

async function carregarDadosEscuderia() {

    const escuderias = await listarEscuderias();

    const escuderia = escuderias.find(
        (e) => e.id_escuderia == idEscuderia
    );


    if (!escuderia) {

        document.getElementById(
            "nomeEscuderia"
        ).textContent =
            "Escuderia não encontrada.";

        return;
    }


    document.getElementById(
        "nomeEscuderia"
    ).innerHTML = `

        ${escuderia.nome_escuderia}

        <br>

        <span id="infoEscuderia">
            ${escuderia.nome_mentor} - ${escuderia.turma}
        </span>

    `;
}

async function montarFormulario() {

    const criterios = await obterCriterios();

    const form =
        document.getElementById("formAvaliacao");


    criterios.forEach((c) => {

        const bloco =
            document.createElement("div");

        bloco.classList.add("bloco-criterio");


        bloco.innerHTML = `

            <strong>
                ${c.descricao}
            </strong>

            <br>

            <label>

                Nota (0 a 10):

                <input
                    type="number"
                    min="0"
                    max="10"
                    step="0.5"
                    id="nota_${c.id_criterio}"
                    required
                >

            </label>

            <br>

            <textarea
                id="comentario_${c.id_criterio}"
                placeholder="O comentário padrão aparecerá automaticamente..."
                style="width: 100%; margin-top: 5px;"
            ></textarea>

        `;


        form.appendChild(bloco);

        const inputNota =
            document.getElementById(
                `nota_${c.id_criterio}`
            );

        const campoComentario =
            document.getElementById(
                `comentario_${c.id_criterio}`
            );


        inputNota.addEventListener("input", () => {

            const valor = inputNota.value;


            if (valor === "") {

                campoComentario.value = "";

                return;

            }


            const nota =
                parseFloat(valor);


            // Proteção contra valor inválido

            if (
                isNaN(nota) ||
                nota < 0 ||
                nota > 10
            ) {

                campoComentario.value = "";

                return;

            }


            campoComentario.value =
                obterComentarioPadrao(
                    c.id_criterio,
                    nota
                );

        });

    });

}

document
    .getElementById("btnEnviar")
    .addEventListener("click", async () => {

        const criterios =
            await obterCriterios();


        for (const c of criterios) {

            const campoNota =
                document.getElementById(
                    `nota_${c.id_criterio}`
                );


            const nota =
                campoNota.value;

            if (nota === "") {

                alert(
                    `Informe a nota do critério "${c.descricao}".`
                );

                campoNota.focus();

                return;
            }


            const comentario =
                document.getElementById(
                    `comentario_${c.id_criterio}`
                ).value;


            const resultado =
                await cadastrarAvaliacao(
                    idEscuderia,
                    idAvaliador,
                    c.id_criterio,
                    parseFloat(nota),
                    comentario
                );


            if (resultado.detail) {

                alert(
                    `Erro no critério "${c.descricao}": ${resultado.detail}`
                );

                return;
            }

        }


        alert(
            "Avaliação enviada com sucesso!"
        );


        window.location.href =
            "escuderiasAvaliadas.html";

    });

carregarDadosEscuderia();

montarFormulario();