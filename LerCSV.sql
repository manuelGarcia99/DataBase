---CSV READER

CREATE TABLE Valores (
Abrantes FLOAT,
Abrantes_Pego FLOAT,
Beja FLOAT,
Braganca FLOAT,
Canas_de_Senhorim FLOAT,
Castelo_Branco FLOAT,
Coimbra FLOAT,
Cunha_Baixa FLOAT,
Elvas FLOAT,
Evora FLOAT,
Faro FLOAT,
Fratel_estacao_submersa FLOAT,
Funchal FLOAT,
Junqueira FLOAT,
Juromenha_estacao_submersa FLOAT,
Lisboa FLOAT,
Meimoa FLOAT,
Mesquitela FLOAT,
Penhas_Douradas FLOAT,
Pocinho_estacao_submersa FLOAT,
Ponta_Delgada FLOAT,
Portalegre FLOAT,
Porto FLOAT,
Reboleiro FLOAT,
Sines FLOAT,
Vila_Real FLOAT



)



BULK INSERT dbo.Valores
FROM 'C:/Users/manec/Desktop/Base de Dados/exemplo.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
)
GO


