-- Criação da view 'fato_locacao', que é a tabela de fatos para as locações.
-- Ela contém os dados principais sobre cada locação, como o ID do cliente, carro, valores, etc.
CREATE VIEW fato_locacao AS
SELECT 
    -- Informações da Locação
    l.idLocacao       AS id_locacao,         
    l.idCliente       AS id_cliente,         
    l.dataLocacao     AS data_locacao,       
    l.horaLocacao     AS hora_locacao,       
    l.idCarro         AS id_carro,           
    l.kmCarro         AS quilometragem_inicial, 
    
    -- Informações da Locação (diária, datas e vendedor)
    l.qtdDiaria       AS quantidade_diaria,  
    l.vlrDiaria       AS valor_diaria,      
    
    l.dataEntrega     AS data_entrega,       
    l.horaEntrega     AS hora_entrega,       
    l.idVendedor      AS id_vendedor         
FROM 
    Locacoes l;  -- A tabela de onde os dados são extraídos (Locacoes)

-- Criação da view 'dim_clientes', que é a tabela de dimensão para os clientes.
-- Ela extrai informações sobre os clientes, como nome, cidade, estado e país.
CREATE VIEW dim_clientes AS 
SELECT DISTINCT 
    idCliente AS id_cliente,          
    nomeCliente AS cliente,           
    cidadeCliente AS cidade,         
    estadoCliente AS estado,        
    paisCliente AS pais              
FROM 
    Clientes c;  -- Tabela de clientes

-- Criação da view 'dim_carros', que é a tabela de dimensão para os carros.
-- Ela contém informações detalhadas sobre os carros, como marca, modelo, ano e quilometragem atual.
CREATE VIEW dim_carros AS
SELECT DISTINCT 
    ca.idCarro AS id_carro,                 
    ca.classiCarro AS classificacao,        
    ca.marcaCarro AS marca,                 
    ca.modeloCarro AS modelo,               
    ca.anoCarro AS ano,                    
    ca.kmCarroatual AS quilometragem_atual,
    ca.idCombustivel AS id_combustivel,    -- ID do tipo de combustível do carro
    co.tipoCombustivel AS tipo_combustivel -- Tipo de combustível (gasolina, etanol, etc.)
FROM 
    Carros ca
JOIN 
    Combustiveis co ON ca.idCombustivel = co.idCombustivel;  -- Junção com a tabela de combustíveis

-- Criação da view 'dim_vendedores', que é a tabela de dimensão para os vendedores.
-- Ela contém informações sobre os vendedores, como nome, sexo e estado.
CREATE VIEW dim_vendedores AS
SELECT DISTINCT 
    idVendedor AS id_vendedor,           
    nomeVendedor AS vendedor,            
    sexoVendedor AS sexo,                
    estadoVendedor AS estado              
FROM  
    Vendedores v;  -- Tabela de vendedores

-- Criação da view 'dim_tempo', que é a tabela de dimensão para o tempo.
-- Ela contém a data e hora das locações e entregas, e formata essas informações.
CREATE VIEW dim_tempo AS
SELECT DISTINCT
    dataLocacao AS data,  -- Data da locação
    -- Formatação da data para extrair ano, mês e dia
    strftime('%Y', substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2)) AS ano,  -- Ano da locação
    strftime('%m', substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2)) AS mes,  -- Mês da locação
    strftime('%d', substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2)) AS dia,  -- Dia da locação
    horaLocacao AS hora,    -- Hora da locação
    'locacao' AS tipo       -- Tipo de evento: 'locacao'
FROM 
    Locacoes
WHERE 
    dataLocacao IS NOT NULL  -- Só considera locações com data

-- União com a segunda parte para incluir as entregas de carros
UNION ALL

SELECT DISTINCT
    dataEntrega AS data,  -- Data da entrega
    -- Formatação da data para extrair ano, mês e dia
    strftime('%Y', substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2)) AS ano,  -- Ano da entrega
    strftime('%m', substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2)) AS mes,  -- Mês da entrega
    strftime('%d', substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2)) AS dia,  -- Dia da entrega
    horaEntrega AS hora,  -- Hora da entrega
    'entrega' AS tipo     -- Tipo de evento: 'entrega'
FROM 
    Locacoes
WHERE 
    dataEntrega IS NOT NULL;  -- Só considera entregas com data
