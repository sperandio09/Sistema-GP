USE sistema_gp;

INSERT INTO tipousuario (id_tipousuario, descricao) VALUES (1, 'Mentor')
INSERT INTO usuario (id_tipousuario, nome) VALUES (1, 'Professor Teste')

SELECT * FROM usuario
SELECT * FROM tipousuario

DESCRIBE escuderia
DESCRIBE usuario
DESCRIBE tipousuario
DESCRIBE avaliacao
DESCRIBE criterio
DESCRIBE divulgacao

SELECT * FROM escuderia