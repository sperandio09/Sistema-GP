USE sistema_gp

INSERT INTO tipousuario (id_tipousuario, descricao) VALUES ('2', 'AVALIADOR')
INSERT INTO usuario (id_tipousuario, nome) VALUES ('2', 'AVALIADOR TESTE')
INSERT INTO criterio (descricao) VALUES ('Inovação')

SELECT * FROM tipousuario
SELECT * FROM usuario
SELECT * FROM escuderia
SELECT * FROM criterio
SELECT * FROM avaliacao