INSERT INTO Paciente (id_paciente, nome, data_nascimento, telefone, telefone2, email, prontuario, id_acompanhante) VALUES
(1, 'Maria Silva', '1985-05-12', '11999998888', NULL, 'maria.silva@email.com', 'PRONT001', NULL),
(2, 'João Souza', '1990-10-30', '11888887777', '11999991111', 'joao.souza@email.com', 'PRONT002', 1), 
(3, 'Ana Pereira', '1978-07-19', '11944443333', NULL, 'ana.pereira@email.com', 'PRONT003', NULL),
(4, 'Carlos Lima', '1982-11-23', '1177776666', '11922223333', 'carlos.lima@email.com', 'PRONT004', 3), 
(5, 'Patrícia Gomes', '1995-02-14', '11888889999', NULL, NULL, 'PRONT005', NULL),
(6, 'Roberto Costa', '1988-09-07', '11955554444', '11955556666', 'roberto.costa@email.com', 'PRONT006', 5), 
(7, 'Fernanda Alves', '1993-12-01', '11777779999', NULL, 'fernanda.alves@email.com', 'PRONT007', NULL),
(8, 'Rafael Martins', '1980-05-18', '11922221111', '11933334444', 'rafael.martins@email.com', 'PRONT008', 7), 
(9, 'Juliana Rocha', '1975-03-27', '11888884444', NULL, 'juliana.rocha@email.com', 'PRONT009', NULL),
(10, 'Marcos Dias', '1987-06-10', '11999990000', '11900001111', NULL, 'PRONT010', 9), (11, 'Carla Fernandes', '1991-01-15', '11777770000', NULL, 'carla.fernandes@email.com', 'PRONT011', NULL),
(12, 'Bruno Moreira', '1983-04-20', '11955557777', '11955558888', 'bruno.moreira@email.com', 'PRONT012', NULL),
(13, 'Simone Nunes', '1979-08-08', '11888882222', NULL, NULL, 'PRONT013', NULL),
(14, 'Lucas Melo', '1994-11-29', '11922220000', '11922229999', 'lucas.melo@email.com', 'PRONT014', NULL),
(15, 'Aline Rocha', '1986-07-07', '11777770001', NULL, 'aline.rocha@email.com', 'PRONT015', NULL),
(16, 'Pedro Albuquerque', '1981-10-16', '11999995555', '11999996666', 'pedro.albuquerque@email.com', 'PRONT016', NULL),
(17, 'Natália Silva', '1992-03-05', '11888881111', NULL, 'natalia.silva@email.com', 'PRONT017', NULL),
(18, 'Felipe Castro', '1984-09-22', '11955552222', '11955553333', NULL, 'PRONT018', NULL),
(19, 'Larissa Costa', '1989-05-30', '11777773333', NULL, 'larissa.costa@email.com', 'PRONT019', NULL),
(20, 'Thiago Alves', '1990-12-12', '11922221112', '11922221113', 'thiago.alves@email.com', 'PRONT020', NULL),
(21, 'Renata Lima', '1987-01-01', '11999991111', NULL, 'renata.lima@email.com', 'PRONT021', NULL),
(22, 'Gustavo Fernandes', '1985-03-19', '11888883333', '11888884444', NULL, 'PRONT022', NULL),
(23, 'Marcela Vieira', '1993-07-25', '11955559999', NULL, 'marcela.vieira@email.com', 'PRONT023', NULL),
(24, 'Eduardo Rocha', '1976-11-11', '11777771111', '11777772222', 'eduardo.rocha@email.com', 'PRONT024', NULL),
(25, 'Vanessa Almeida', '1982-02-28', '11922223333', NULL, NULL, 'PRONT025', NULL),
(26, 'Rogério Martins', '1980-08-15', '11999992222', '11999993333', 'rogerio.martins@email.com', 'PRONT026', NULL),
(27, 'Amanda Souza', '1991-06-17', '11888884444', NULL, 'amanda.souza@email.com', 'PRONT027', NULL),
(28, 'Felipe Santos', '1983-09-09', '11955554444', '11955556666', NULL, 'PRONT028', NULL),
(29, 'Bianca Lopes', '1995-04-21', '11777770002', NULL, 'bianca.lopes@email.com', 'PRONT029', NULL),
(30, 'Diego Fernandes', '1988-12-03', '11922220001', '11922220002', 'diego.fernandes@email.com', 'PRONT030', NULL);

INSERT INTO Medico (id_medico, nome, CRM, telefone1, telefone2, especialidade) VALUES
(1, 'Dr. João Almeida', 'CRM12345', '11999990001', NULL, 'Cardiologia'),
(2, 'Dra. Maria Fernandes', 'CRM12346', '11999990002', '11999990003', 'Pediatria'),
(3, 'Dr. Carlos Silva', 'CRM12347', NULL, NULL, 'Ortopedia'),
(4, 'Dra. Ana Souza', 'CRM12348', '11888881111', NULL, 'Dermatologia'),
(5, 'Dr. Roberto Lima', 'CRM12349', '11922223333', '11922224444', 'Ginecologia'),
(6, 'Dra. Fernanda Costa', 'CRM12350', '11777772222', NULL, 'Neurologia'),
(7, 'Dr. Lucas Martins', 'CRM12351', '11955556666', '11955557777', 'Endocrinologia'),
(8, 'Dra. Juliana Rocha', 'CRM12352', NULL, '11900001111', 'Oftalmologia'),
(9, 'Dr. Pedro Carvalho', 'CRM12353', '11888889999', NULL, 'Psiquiatria'),
(10, 'Dra. Camila Dias', 'CRM12354', '11999993333', '11999994444', 'Urologia'),
(11, 'Dr. Ricardo Almeida', 'CRM12355', '11911112222', NULL, 'Radiologia'),
(12, 'Dra. Sandra Oliveira', 'CRM12356', '11822223333', '11822224444', 'Radiologia');

INSERT INTO Enfermeira (id_enfermeira, COREN, nome, telefone1, telefone2, email) VALUES
(1, 'COREN1001', 'Ana Paula', '11999990001', NULL, 'ana.paula@email.com'),
(2, 'COREN1002', 'Carlos Mendes', '11888881111', '11888882222', NULL),
(3, 'COREN1003', 'Fernanda Alves', '11777770000', NULL, 'fernanda.alves@email.com'),
(4, 'COREN1004', 'Marcos Dias', '11922223333', '11922224444', 'marcos.dias@email.com'),
(5, 'COREN1005', 'Patrícia Gomes', '11955556666', NULL, NULL),
(6, 'COREN1006', 'Roberto Costa', '11999991111', '11999992222', 'roberto.costa@email.com'),
(7, 'COREN1007', 'Juliana Rocha', '11888883333', NULL, 'juliana.rocha@email.com'),
(8, 'COREN1008', 'Bruno Moreira', '11777772222', '11777773333', NULL),
(9, 'COREN1009', 'Larissa Costa', '11900001111', NULL, 'larissa.costa@email.com'),
(10, 'COREN1010', 'Thiago Alves', '11955559999', '11955558888', 'thiago.alves@email.com');

INSERT INTO Sala (id_sala, numero, bloco, data_manutencao, capacidade) VALUES
(1, 101, 'A', '2024-01-15', 20),
(2, 102, 'A', NULL, 15),
(3, 201, 'B', '2023-12-10', 30),
(4, 202, 'B', NULL, NULL),
(5, 301, 'C', '2024-02-20', 25),
(6, 302, 'C', '2023-11-05', NULL),
(7, 401, 'D', NULL, 18),
(8, 402, 'D', '2024-03-12', 22),
(9, 501, 'E', NULL, NULL),
(10, 502, 'E', '2023-10-30', 16);

INSERT INTO Equipamento (id_equipamento, id_sala, nome, modelo, data_manutencao, classificacao_risco) VALUES
(1, 1, 'Esfigmomanômetro', 'Modelo X', '2024-01-15', 'Baixo'),
(2, 1, 'Balança', 'Modelo Y', '2023-12-10', 'Baixo'),
(3, 1, 'Termômetro', 'EnferModel 1', '2023-11-05', 'Baixo'),
(4, 1, 'Esfigmomanômetro', 'EnferModel 2', '2024-01-10', 'Baixo'),
(5, 3, 'Espéculo', 'GyneModel 1', '2024-02-20', 'Baixo'),
(6, 3, 'Colposcópio', 'GyneModel 2', '2023-11-05', 'Médio'),
(7, 4, 'Oftalmoscópio', 'NeuroModel 1', '2023-11-05', 'Baixo'),
(8, 4, 'Diapasão', 'NeuroModel 2', '2024-01-01', 'Baixo'),
(9, 5, 'Bisturi', 'DermaModel 1', '2023-10-30', 'Alto'),
(10, 5, 'Materiais Cirúrgicos', 'DermaKit 3', '2024-02-15', 'Alto');

INSERT INTO Ultrassom (id_ultrassom, modelo, fabricante, data_manutencao, responsavel_tecnico, id_sala) VALUES
(1, 'UltraModel 1', 'UltraTech', '2024-02-15', 'Técnico A', 9),
(2, 'UltraModel 2', 'UltraTech', '2023-12-01', 'Técnico B', 10);

INSERT INTO Medicamento (id_medicamento, nome, fabricante, estoque, preco, validade) VALUES
(1, 'Paracetamol 500mg', 'Farmaceutica A', 75, 10.00, '2025-12-31'),
(2, 'Dipirona 1g', 'Farmaceutica B', 60, 15.00, '2024-11-30'),
(3, 'Ibuprofeno 400mg', 'Farmaceutica C', 120, 12.00, '2025-06-30'),
(4, 'AAS 100mg', 'Farmaceutica D', 90, 8.50, '2025-08-31'),
(5, 'Losartana 50mg', 'Farmaceutica E', 55, 35.00, '2026-01-31'),
(6, 'Metformina 850mg', 'Farmaceutica F', 110, 25.00, '2025-05-31'),
(7, 'Glimepirida 2mg', 'Farmaceutica G', 70, 40.00, '2025-09-30'),
(8, 'Loratadina 10mg', 'Farmaceutica H', 80, 18.00, '2024-12-31'),
(9, 'Clonazepam 2mg', 'Farmaceutica I', 65, 50.00, '2025-07-31'),
(10, 'Ranitidina 150mg', 'Farmaceutica J', 100, 22.00, '2024-10-31'),
(11, 'Amiodarona 200mg', 'Farmaceutica K', 85, 55.00, '2025-03-31'),
(12, 'Captopril 25mg', 'Farmaceutica L', 95, 30.00, '2025-04-30'),
(13, 'Cetirizina 10mg', 'Farmaceutica M', 72, 20.00, '2026-02-28'),
(14, 'Omeprazol 20mg', 'Farmaceutica N', 58, 28.00, '2025-11-30'),
(15, 'Clindamicina 300mg', 'Farmaceutica O', 105, 45.00, '2025-09-30'),
(16, 'Prednisona 20mg', 'Farmaceutica P', 68, 27.00, '2025-12-31'),
(17, 'Dexametasona 4mg', 'Farmaceutica Q', 62, 32.00, '2026-01-31'),
(18, 'Salbutamol 100mcg', 'Farmaceutica R', 77, 24.00, '2025-05-31'),
(19, 'Levotiroxina 50mcg', 'Farmaceutica S', 66, 33.00, '2025-08-31'),
(20, 'Nifedipino 30mg', 'Farmaceutica T', 59, 37.00, '2026-03-31'),
(21, 'Omeprazol 40mg', 'Farmaceutica U', 88, 30.00, '2026-02-28'),
(22, 'Ranitidina 300mg', 'Farmaceutica V', 95, 25.00, '2025-07-31'),
(23, 'Fluconazol 150mg', 'Farmaceutica W', 85, 50.00, '2025-11-30'),
(24, 'Dipropionato de Betametasona 0,05%', 'Farmaceutica X', 78, 30.00, '2025-10-31'),
(25, 'Naproxeno 250mg', 'Farmaceutica Y', 90, 19.00, '2025-09-30'),
(26, 'Cetoconazol 200mg', 'Farmaceutica Z', 69, 44.00, '2026-01-31'),
(27, 'Morfofina 10mg', 'Farmaceutica AA', 100, 65.00, '2025-06-30'),
(28, 'Glimepirida 2mg', 'Farmaceutica BB', 55, 42.00, '2025-12-31'),
(29, 'Clopidogrel 75mg', 'Farmaceutica CC', 61, 70.00, '2026-04-30'),
(30, 'Ibuprofeno 600mg', 'Farmaceutica DD', 73, 20.00, '2025-08-31');

INSERT INTO Acolhimento (id_acolhimento, id_enfermeira, id_paciente, data_hora, peso, altura, pressao_arterial, temperatura) VALUES
(1, 1, 1, '2024-06-01 08:30:00', 70.5, 1.75, '120/80', 36.7),
(2, 2, 2, '2024-06-01 09:00:00', 65.0, 1.68, '110/70', 36.5),
(3, 3, 3, '2024-06-02 10:15:00', 80.2, 1.80, '130/85', 37.0),
(4, 4, 4, '2024-06-02 11:45:00', 55.3, 1.60, '115/75', 36.6),
(5, 5, 5, '2024-06-03 08:00:00', 90.0, 1.85, '140/90', 37.2),
(6, 6, 6, '2024-06-03 09:30:00', 72.4, 1.70, '125/82', 36.8),
(7, 7, 7, '2024-06-04 14:00:00', 68.0, 1.72, '118/78', 36.4),
(8, 8, 8, '2024-06-04 15:30:00', 77.1, 1.78, '122/80', 36.9);

INSERT INTO Consulta (id_consulta, id_medico, id_paciente, id_sala, data_hora, CID11, valor, forma_pagamento, consulta_descritiva) VALUES
(1, 1, 1, 1, '2024-06-05 10:00:00', 'I10', 150.00, 'Cartão', 'Paciente hipertenso, relata dor torácica leve. PA alta, sem sinais de urgência.'),
(2, 2, 2, 2, '2024-06-05 11:30:00', 'J45', 200.00, 'Dinheiro', 'Asma com tosse seca e chiado. Prescrito broncodilatador.'),
(3, 3, 3, 3, '2024-06-06 08:45:00', 'M16', 180.00, 'Cartão', 'Dor no joelho direito, quadro crônico, sem trauma recente.'),
(4, 4, 4, 4, '2024-06-06 09:15:00', 'L20', 160.00, 'Convênio', 'Dermatite atópica ativa com placas pruriginosas. Prescrito corticosteroide tópico.'),
(5, 5, 5, 5, '2024-06-07 14:00:00', 'N93', 210.00, 'Cartão', 'Dor pélvica e sangramento irregular. Solicitada ultrassonografia.'),
(6, 6, 6, 6, '2024-06-07 15:30:00', 'G40', 190.00, 'Dinheiro', 'Crises convulsivas recentes, iniciada medicação anticonvulsivante.'),
(7, 7, 7, 7, '2024-06-08 13:00:00', 'E11', 170.00, 'Convênio', 'Diabetes tipo 2 com controle instável, solicitados exames.'),
(8, 8, 8, 8, '2024-06-08 14:30:00', 'H25', 220.00, 'Cartão', 'Visão reduzida progressiva, suspeita de glaucoma, iniciado tratamento.');

INSERT INTO Prescricao (id_consulta, id_medicamento, dosagem, quantidade, duracao, periodicidade, necessita_alimentacao, horario_especifico) VALUES
(1, 5, '50mg', 10, 30, '1x ao dia', FALSE, '08:00:00'),
(2, 2, '1g', 5, 5, '3x ao dia', TRUE, '12:00:00'),
(3, 25, '250mg', 7, 10, '2x ao dia', FALSE, '08:00:00'),
(4, 15, '300mg', 8, 7, '2x ao dia', TRUE, '18:00:00'),
(5, 16, '20mg', 12, 14, '1x ao dia', FALSE, NULL),
(6, 9, '2mg', 15, 20, '1x ao dia', FALSE, '20:00:00'),
(7, 7, '850mg', 20, 60, '2x ao dia', TRUE, '07:00:00'),
(8, 13, '10mg', 25, 7, '1x ao dia', FALSE, NULL);

INSERT INTO Vacina (id_vacina, id_acolhimento, fabricante, validade, dose_recomendada, nome) VALUES
(1, 1, 'Fabricante A', '2025-12-31', 2, 'Vacina Hepatite B'),
(2, 4, 'Fabricante D', '2025-08-31', 2, 'Vacina HPV');

INSERT INTO Alergia (id_alergia, id_paciente, nome, gravidade, tem_tolerancia_exposicao, dose_segura) VALUES
(1, 1, 'Alergia a Penicilina', 3, FALSE, NULL),
(2, 1, 'Alergia a Amoxicilina', 2, TRUE, 0.02),
(3, 1, 'Alergia a Pólen', 1, TRUE, 0.10),
(4, 3, 'Alergia a Amendoim', 4, FALSE, NULL),
(5, 5, 'Alergia a Látex', 2, TRUE, 0.05),
(6, 7, 'Alergia a Pólen', 1, TRUE, 0.10),
(7, 9, 'Alergia a Sulfa', 3, FALSE, NULL);
