-- Criação das Tabelas

-- Criação da tabela 'Combustiveis', que armazena os tipos de combustíveis disponíveis.
-- Cada tipo de combustível terá um ID único (idCombustivel) e o nome do tipo de combustível (tipoCombustivel).
CREATE TABLE Combustiveis (
    idCombustivel INT PRIMARY KEY,         
    tipoCombustivel VARCHAR(50)            
);

-- Criação da tabela 'Carros', que armazena os carros disponíveis para locação.
-- Esta tabela faz referência à tabela 'Combustiveis', associando cada carro a um tipo de combustível.
CREATE TABLE Carros (
    idCarro INT PRIMARY KEY,              
    classiCarro VARCHAR(50),              
    modeloCarro VARCHAR(100),              
    anoCarro INT,                          
    idCombustivel INT,                     
    FOREIGN KEY (idCombustivel) REFERENCES Combustiveis(idCombustivel)  -- Chave estrangeira para a tabela 'Combustiveis'
);

-- Criação da tabela 'Clientes', que armazena os clientes que realizam locações.
-- Contém informações como nome, cidade, estado e país do cliente.
CREATE TABLE Clientes (
    idCliente INT PRIMARY KEY,             
    nomeCliente VARCHAR(100),              
    cidadeCliente VARCHAR(100),         
    estadoCliente VARCHAR(50),             
    paisCliente VARCHAR(50)                -
);

-- Criação da tabela 'Vendedores', que armazena os vendedores que realizam as locações.
-- Contém informações como nome, sexo e estado do vendedor.
CREATE TABLE Vendedores (  
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor VARCHAR(10),
    estadoVendedor VARCHAR(50)     
);

-- Criação da tabela 'Locacoes', que armazena as locações feitas pelos clientes.
-- Contém dados como quilometragem inicial do carro, data e hora da locação, valor da diária, etc.
-- Referências para as tabelas 'Clientes', 'Carros' e 'Vendedores' são usadas.
CREATE TABLE Locacoes (
    idLocacao INT PRIMARY KEY,             
    idCliente INT,                        
    idCarro INT,                           
    kmCarro DECIMAL(10, 2),              
    dataLocacao DATE,                     
    horaLocacao TIME,                    
    qtdDiaria INT,                         
    vlrDiaria DECIMAL(10, 2),           
    dataEntrega DATE,                     
    idVendedor INT,                        
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),     
    FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),           
    FOREIGN KEY (idVendedor) REFERENCES Vendedores(idVendedor)  
);

-- Inserção de Dados na tabela 'Locacoes' a partir da tabela 'tb_locacao' (provavelmente uma tabela de origem).
-- Os dados são inseridos na tabela de locações sem duplicidade (DISTINCT).
INSERT INTO Locacoes (
    idLocacao, 
    idCliente, 
    idCarro,
    kmCarro,
    dataLocacao, 
    horaLocacao, 
    qtdDiaria,
    vlrDiaria,
    dataEntrega,
    horaEntrega,
    idVendedor
)
SELECT 
    DISTINCT 
    idLocacao,               
    idCliente,               
    idCarro,
    kmCarro,
    dataLocacao,             
    horaLocacao,             
    qtdDiaria,               
    vlrDiaria,               
    dataEntrega,             
    horaEntrega,             
    idVendedor               
FROM 
    tb_locacao;  -- A origem dos dados é a tabela 'tb_locacao'

-- Inserção de Dados na tabela 'Vendedores', a partir da tabela 'tb_locacao', sem duplicidade.
-- Insere os vendedores únicos presentes na tabela de origem.
INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;  -- A origem dos dados é a tabela 'tb_locacao'

-- Inserção de Dados na tabela 'Clientes', a partir da tabela 'tb_locacao', sem duplicidade.
-- Insere os clientes únicos presentes na tabela de origem.
INSERT INTO Clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;  -- A origem dos dados é a tabela 'tb_locacao'

-- Inserção de Dados na tabela 'Carros', a partir da tabela 'tb_locacao', sem duplicidade.
-- Insere os carros únicos presentes na tabela de origem.
-- A instrução 'INSERT OR IGNORE' impede a inserção de registros duplicados.
INSERT OR IGNORE INTO Carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;  -- A origem dos dados é a tabela 'tb_locacao'

-- Inserção de Dados na tabela 'Combustiveis', a partir da tabela 'tb_locacao', sem duplicidade.
-- Insere os combustíveis únicos presentes na tabela de origem.
INSERT INTO Combustiveis (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;  -- A origem dos dados é a tabela 'tb_locacao'