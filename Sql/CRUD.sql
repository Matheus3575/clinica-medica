-- ========================
-- INSERT: Cadastro de 3 pacientes
-- ========================
INSERT INTO Paciente (id_paciente, nome, data_nascimento, telefone, telefone2, email, prontuario) VALUES
(101, 'Luccas dos Anjos', '1995-04-10', '11999998888', NULL, 'lucas.anjos@example.com', 'PACI0101'),
(102, 'Maria Olivia', '1987-12-05', '11911112222', NULL, 'maria.olivia@example.com', 'PACI0102'),
(103, 'João Vieira', '1978-06-20', '11777778888', NULL, 'joao.vieira@example.com', 'PACI0103');


-- ========================
-- INSERT: Consultas para cada paciente
-- ========================
INSERT INTO Consulta (id_consulta, id_medico, id_paciente, id_sala, data_hora, CID11, valor, forma_pagamento, consulta_descritiva)
VALUES 
(201, 4, 101, 3, '2025-06-30 08:30:00', 'L20', 200.00, 'Cartão', NULL),
(202, 4, 102, 3, '2025-06-30 09:00:00', 'B34', 180.00, 'Dinheiro', 'Queixa de tosse seca persistente e dificuldade respiratória leve.'),
(203, 4, 103, 3, '2025-06-30 09:30:00', 'R51', 220.00, 'Cartão', 'Paciente relata dor de cabeça frequente, sem sinais neurológicos evidentes.');


-- ========================
-- INSERT: Alergias para paciente 103 (paciente vivo, consulta ativa)
-- ========================

INSERT INTO Alergia (id_alergia, id_paciente, nome, gravidade, tem_tolerancia_exposicao, dose_segura)
VALUES 
(11, 103, 'Penicilina', 4, FALSE, 0.00),
(12, 103, 'Amendoim', 3, TRUE, 5.00);


-- ========================
-- DELETE: Paciente faleceu (sem alergias registradas)
-- ========================

DELETE FROM Consulta WHERE id_paciente = 101;
DELETE FROM Paciente WHERE id_paciente = 101;


-- ========================
-- UPDATE: Corrigir nome da paciente 102
-- ========================

UPDATE Paciente
SET nome = 'Maria Olívia'
WHERE id_paciente = 102;


-- ========================
-- SELECT: Verificar alergias do paciente 103
-- ========================

SELECT a.nome AS alergia, a.gravidade, a.dose_segura
FROM Alergia a
JOIN Paciente p ON a.id_paciente = p.id_paciente
WHERE p.id_paciente = 103;