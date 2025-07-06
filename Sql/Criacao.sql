CREATE TABLE Paciente (
id_paciente INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
data_nascimento DATE NOT NULL,
telefone VARCHAR(20),
telefone2 VARCHAR(20),
email VARCHAR(100),
prontuario VARCHAR(50) NOT NULL UNIQUE,
id_acompanhante INT NULL,
CONSTRAINT fk_acompanhante FOREIGN KEY (id_acompanhante) REFERENCES Paciente(id_paciente)
);

CREATE TABLE Enfermeira (
 id_enfermeira INT PRIMARY KEY,
 COREN VARCHAR(20) NOT NULL UNIQUE,
 nome VARCHAR(100) NOT NULL,
 telefone1 VARCHAR(20),
 telefone2 VARCHAR(20),
 email VARCHAR(100)
);
CREATE TABLE Acolhimento (
 id_acolhimento INT PRIMARY KEY,
 id_enfermeira INT NOT NULL,
 id_paciente INT NOT NULL,
 data_hora DATETIME NOT NULL,
 peso DECIMAL(5,2) NOT NULL,
 altura DECIMAL(4,2) NOT NULL,
 pressao_arterial VARCHAR(10),
 temperatura DECIMAL(4,2),
 FOREIGN KEY (id_enfermeira) REFERENCES Enfermeira(id_enfermeira),
 FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);
CREATE TABLE Vacina (
 id_vacina INT PRIMARY KEY,
 id_acolhimento INT NOT NULL,
 fabricante VARCHAR(100) NOT NULL,
 validade DATE,
 dose_recomendada INT,
 nome VARCHAR(100) NOT NULL,
 FOREIGN KEY (id_acolhimento) REFERENCES Acolhimento(id_acolhimento)
);
CREATE TABLE Medico (
 id_medico INT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 CRM VARCHAR(20) NOT NULL UNIQUE,
 telefone1 VARCHAR(20),
 telefone2 VARCHAR(20),
 especialidade VARCHAR(100)
);
CREATE TABLE Consulta (
 id_consulta INT PRIMARY KEY,
 id_medico INT NOT NULL,
 id_paciente INT NOT NULL,
 id_sala INT NOT NULL,
 data_hora DATETIME NOT NULL,
 CID11 VARCHAR(10) NOT NULL,
 valor DECIMAL(10,2),
 forma_pagamento VARCHAR(50),
 consulta_descritiva TEXT,
 FOREIGN KEY (id_medico) REFERENCES Medico(id_medico),
 FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
 FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
);
CREATE TABLE Alergia (
 id_alergia INT PRIMARY KEY,
 id_paciente INT NOT NULL,
 nome VARCHAR(100) NOT NULL,
 gravidade INT NOT NULL,
 tem_tolerancia_exposicao BOOLEAN,
 dose_segura DECIMAL(10,2),
 FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);
CREATE TABLE Medicamento (
 id_medicamento INT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 fabricante VARCHAR(100) NOT NULL,
 estoque INT NOT NULL DEFAULT 50,
 preco DECIMAL(10,2),
 validade DATE
);

CREATE TABLE Prescricao (
    id_consulta INT NOT NULL,
    id_medicamento INT NOT NULL,
    dosagem VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,  
    duracao INT NOT NULL,
    periodicidade VARCHAR(50) NOT NULL,
    necessita_alimentacao BOOLEAN,
    horario_especifico TIME,
    PRIMARY KEY (id_consulta, id_medicamento),
    FOREIGN KEY (id_consulta) REFERENCES Consulta(id_consulta),
    FOREIGN KEY (id_medicamento) REFERENCES Medicamento(id_medicamento)
);


CREATE TABLE Sala (
 id_sala INT PRIMARY KEY,
 numero INT NOT NULL,
 bloco VARCHAR(10) NOT NULL,
 data_manutencao DATE,
 capacidade INT
);
CREATE TABLE Equipamento (
 id_equipamento INT PRIMARY KEY,
 id_sala INT NOT NULL,
 nome VARCHAR(100) NOT NULL,
 modelo VARCHAR(100) NOT NULL,
 data_manutencao DATE,
 classificacao_risco VARCHAR(50),
 FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
);
CREATE TABLE Ultrassom (
 id_ultrassom INT PRIMARY KEY,
 modelo VARCHAR(100) NOT NULL,
 fabricante VARCHAR(100) NOT NULL,
 data_manutencao DATE,
 responsavel_tecnico VARCHAR(100),
 id_sala INT NOT NULL UNIQUE,
 FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
);