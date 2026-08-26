USE sistema_gp

INSERT INTO tipousuario (id_tipousuario, descricao) VALUES ('3', 'ALUNO')
INSERT INTO usuario (id_tipousuario, nome) VALUES ('2', 'AVALIADOR TESTE')
INSERT INTO criterio (descricao) VALUES ('Inovação')

SELECT * FROM tipousuario
SELECT * FROM usuario
SELECT * FROM escuderia
SELECT * FROM criterio
SELECT * FROM avaliacao

DELETE FROM escuderia
DELETE FROM usuario
DELETE FROM criterio
DELETE FROM avaliacao
