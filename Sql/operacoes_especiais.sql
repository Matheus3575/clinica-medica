-- Consulta 1: Busca com Substring (case insensitive)
SELECT id_medicamento, nome, preco, fabricante
FROM Medicamento
WHERE nome LIKE '%aas%' COLLATE NOCASE;

-- Consulta 2: Operação de Pesquisa
-- Listar pacientes com IMC maior que 25 (sobrepeso)
SELECT p.nome, a.peso, a.altura,
       ROUND(a.peso / (a.altura * a.altura), 2) AS imc
FROM Paciente p
JOIN Acolhimento a ON p.id_paciente = a.id_paciente
WHERE (a.peso / (a.altura * a.altura)) > 25;

-- Consulta 3: Consulta avançada com JOIN (1:N e LEFT JOIN)
-- Listar todos os pacientes, seus prontuários e suas alergias (incluindo pacientes sem alergias)
SELECT p.nome AS paciente, p.prontuario, a.nome AS alergia
FROM Paciente p
LEFT JOIN Alergia a ON p.id_paciente = a.id_paciente
ORDER BY p.nome;

-- Consulta 4: Consulta avançada com JOIN e filtro por data e idade
-- Listar pacientes com mais de 65 anos que têm consultas futuras agendadas
SELECT DISTINCT p.nome, p.data_nascimento, c.data_hora
FROM Paciente p
JOIN Consulta c ON p.id_paciente = c.id_paciente
WHERE p.data_nascimento <= DATE('now', '-65 years')
  AND c.data_hora > DATETIME('now');

-- Consulta 5: Consulta avançada com UNION de duas tabelas e filtro por data
-- Listar salas com equipamentos ou ultrassons cuja última manutenção foi há mais de 5 anos
SELECT s.id_sala, s.numero, s.bloco, e.nome AS equipamento, e.data_manutencao
FROM Sala s
JOIN Equipamento e ON s.id_sala = e.id_sala
WHERE e.data_manutencao <= DATE('now', '-5 years')

UNION

SELECT s.id_sala, s.numero, s.bloco, 'Ultrassom' AS equipamento, u.data_manutencao
FROM Sala s
JOIN Ultrassom u ON s.id_sala = u.id_sala
WHERE u.data_manutencao <= DATE('now', '-5 years');

-- Consulta 6: Ordenação e pesquisa
-- Listar medicamentos ordenados pelo preço, do mais barato ao mais caro
SELECT id_medicamento, nome, preco
FROM Medicamento
ORDER BY preco ASC;

-- Gatilho: Atualiza estoque após inserção na tabela Prescricao
-- Gatilho acionado após inserir uma prescrição, decrementa estoque do medicamento correspondente
CREATE TRIGGER atualiza_estoque_prescricao
AFTER INSERT ON Prescricao
FOR EACH ROW
BEGIN
    UPDATE Medicamento
    SET estoque = estoque - NEW.quantidade
    WHERE id_medicamento = NEW.id_medicamento
    AND estoque >= NEW.quantidade;  -- Impede estoque negativo
END;

-- Teste

SELECT id_medicamento, nome, estoque FROM Medicamento WHERE id_medicamento = 2;

INSERT INTO Prescricao (id_consulta, id_medicamento, dosagem, quantidade, duracao, periodicidade, necessita_alimentacao, horario_especifico)
VALUES (1, 2, '500mg', 5, 5, '2x ao dia', FALSE, '08:00:00');

SELECT id_medicamento, nome, estoque FROM Medicamento WHERE id_medicamento = 2;

-- Consulta com Quantificador ALL
-- Retorna prescrições cuja dosagem é maior que alguma dosagem anterior do mesmo medicamento
SELECT p1.id_consulta, p1.id_medicamento, p1.dosagem
FROM Prescricao p1
WHERE CAST(REPLACE(p1.dosagem, 'mg', '') AS INTEGER) > ALL (
    SELECT CAST(REPLACE(p2.dosagem, 'mg', '') AS INTEGER)
    FROM Prescricao p2
    WHERE p2.id_medicamento = p1.id_medicamento
      AND p2.id_consulta <> p1.id_consulta
);


-- Consulta recursiva que encontra todos os acompanhantes do paciente 2
WITH RECURSIVE Acompanhantes AS (
    SELECT p.id_paciente, p.nome, p.prontuario, p.id_acompanhante
    FROM Paciente p
    WHERE p.id_paciente = 2  -- paciente base

    UNION ALL

    SELECT p2.id_paciente, p2.nome, p2.prontuario, p2.id_acompanhante
    FROM Paciente p2
    INNER JOIN Acompanhantes a ON p2.id_paciente = a.id_acompanhante
)
-- Agora buscamos as consultas feitas pelos acompanhantes 
SELECT c.id_consulta, p.nome, p.prontuario, c.data_hora
FROM Consulta c
JOIN Paciente p ON p.id_paciente = c.id_paciente
WHERE p.id_paciente IN (
    SELECT id_acompanhante FROM Acompanhantes WHERE id_acompanhante IS NOT NULL
);

-- Histórico de consultas do paciente(Agrupamento + HAVING)
SELECT p.nome, c.consulta_descritiva, c.data_hora
FROM Consulta c
JOIN Paciente p ON c.id_paciente = p.id_paciente
WHERE c.id_consulta IN (
    SELECT id_consulta
    FROM (
        SELECT id_consulta,
               ROW_NUMBER() OVER (PARTITION BY id_paciente ORDER BY data_hora DESC) AS rn
        FROM Consulta
        WHERE id_paciente IN (
            SELECT id_paciente
            FROM Consulta
            GROUP BY id_paciente
            HAVING COUNT(*) > 1
        )
    ) sub
    WHERE rn = 1
);
