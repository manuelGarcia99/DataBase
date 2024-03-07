-- Pesquisar Cidade pelo nome da cidade começado por "Co":
SELECT *
FROM Lugar
WHERE Distrito LIKE 'Co%';

-- Pesquisar por Medicoes mais recentes:
SELECT *
FROM Medicoes
ORDER BY DataMedicao DESC;

-- Pesquisar por cidades na base de dados:
SELECT DISTINCT Distrito
FROM Lugar;

-- Media de radiacao por Estacao, no ultimo ano
SELECT E.IDE, L.Distrito , AVG(M.RadLevel) AS Media_de_radiacao
FROM Estacoes E INNER JOIN Lugar L ON L.IDE = E.IDE INNER JOIN Medicoes M ON L.IDL = M.IDL
GROUP BY E.IDE, L.Distrito
'''
SELECT e.*, l.Distrito, l.CoordX, l.CoordY, COALESCE(lm.AvgRadLevel, 0) AS MediaRadiacao
FROM Estacoes e
INNER JOIN Lugar l ON e.IDE = l.IDE
LEFT JOIN LastYearMedicoes lm ON e.IDE = lm.IDE
ORDER BY MediaRadiacao DESC;
'''

-- Pesquisar Estacoes cuja radiacao seja superior a 10% em relacao ao valor medio anual para essa mesma Estacao
SELECT E.IDE, L.Distrito, AVG(M.RadLevel) AS Media_de_radiacao
FROM Estacoes E INNER JOIN Lugar L ON L.IDE = E.IDE INNER JOIN Medicoes M ON L.IDL = M.IDL
WHERE (SELECT MAX(M2.RadLevel) FROM Medicoes M2 WHERE L.IDL = M2.IDL) > 1.1 * (SELECT AVG(M3.RadLevel) FROM Medicoes M3 WHERE L.IDL = M3.IDL)
GROUP BY E.IDE, L.Distrito
'''
SELECT e.*, l.Distrito, l.CoordX, l.CoordY, m.DataMedicao, m.RadLevel
FROM Estacoes e
INNER JOIN Lugar l ON e.IDE = l.IDE
INNER JOIN Sensor s ON e.IDE = s.IDE
INNER JOIN Medicoes m ON s.IDS = m.IDS
INNER JOIN AvgRadiationPerStation ar ON e.IDE = ar.IDE
WHERE m.RadLevel > 1.1 * ar.AvgRadLevel
ORDER BY e.IDE, m.DataMedicao DESC;
'''

-- Estacoes mais novas ate as mais antigas
SELECT * 
FROM Estacoes
ORDER BY DataInstalacao DESC

-- *********************************************************************

-- Adicionar um Lugar
INSERT INTO Lugar (Distrito, NivelMedio, CoordX, CoordY, IDE)
VALUES ('NewCity', 5.0, 30.0, 20.0, 1);


-- create a TABLE for neighboors relationships 
CREATE TABLE Vizinhos (
  IDVizinho INT IDENTITY(1,1) PRIMARY KEY,
  LugarID1 INT,
  LugarID2 INT,
  FOREIGN KEY (LugarID1) REFERENCES Lugar(IDL)
  ON UPDATE CASCADE
  ON DELETE CASCADE,
  FOREIGN KEY (LugarID2) REFERENCES Lugar(IDL)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

-- Insert a neighbor relationship:
INSERT INTO Vizinhos (LugarID1, LugarID2)
VALUES (1, 2);

-- Now, when you want to query whether a certain Lugar is a neighbor of another Lugar, you can check the Vizinhos table:
SELECT *
FROM Vizinhos
WHERE (LugarID1 = 1 AND LugarID2 = 2) OR (LugarID1 = 2 AND LugarID2 = 1);
 
-- *********************************************************************
/*To find and establish neighbor relationships between Lugar entries based on their geographical coordinates,
you can use a query that calculates the distance between each pair of Lugar entries and then considers them
neighbors if the distance is less than 100 kilometers. Here's an example query using the Haversine formula,
which is commonly used to calculate distances between two sets of geographical coordinates:*/
-- Create a temporary table to store pairs of lugares that are less than 100km apart
CREATE TABLE TempVizinhos (
  LugarID1 INT,
  LugarID2 INT,
  PRIMARY KEY (LugarID1, LugarID2)
);

-- Insert pairs of lugares that are less than 100km apart into the temporary table
INSERT INTO TempVizinhos (LugarID1, LugarID2)
SELECT l1.IDL AS LugarID1, l2.IDL AS LugarID2
FROM Lugar l1
JOIN Lugar l2 ON l1.IDL < l2.IDL -- Avoid duplicate pairs
WHERE SQRT((l1.CoordX - l2.CoordX) * (l1.CoordX - l2.CoordX) + (l1.CoordY - l2.CoordY) + (l1.CoordY - l2.CoordY)) < 100;

-- Update the Vizinhos table with the temporary data
INSERT INTO Vizinhos (LugarID1, LugarID2)
SELECT LugarID1, LugarID2 FROM TempVizinhos;

-- Drop the temporary table
DROP TABLE TempVizinhos;
-- *********************************************************************
-- Pesquisar Medicoes cuja data é mais recente do que uma certa data
SELECT *
FROM Medicoes
WHERE DataMedicao > '2023-01-01'; -- Replace '2023-01-01' with your desired date

-- Pesquisar NivelAlerta cujo valor é maior do que um certo valor
SELECT *
FROM Medicoes
WHERE NivelAlerta > 2; -- Replace 2 with your desired value
-- *********************************************************************
-- Pesquisar todos os Lugares que sao vizinhos de um certo Lugar 
DECLARE @TargetLugarID INT = 1; -- Replace with the desired LugarID

SELECT DISTINCT L.IDL , L.Distrito
FROM Vizinhos v INNER JOIN Lugar L ON L.IDL = v.LugarID1 OR L.IDL = v.LugarID2
WHERE v.LugarID1 = @TargetLugarID OR v.LugarID2 = @TargetLugarID;
-- *********************************************************************
/* If the user may provide values for Marca and/or Tipo_sensor,
and you want to retrieve rows based on the provided information, you can use the following query:*/
DECLARE @UserMarca NVARCHAR(50) = NULL; -- Replace with the user's choice for Marca or leave as NULL
DECLARE @UserTipoSensor NVARCHAR(50) = '70013A GM'; -- Replace with the user's choice for Tipo_sensor or leave as NULL

SELECT *
FROM Sensor
WHERE (Marca = @UserMarca OR @UserMarca IS NULL OR Marca = '')
   AND (Tipo_sensor = @UserTipoSensor OR @UserTipoSensor IS NULL OR Tipo_sensor = '');


