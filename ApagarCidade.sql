
DELETE FROM Estacoes 
WHERE IDE = 2
DELETE FROM Sensor 
WHERE IDE = 1
-- ver se ao apagar esta��es podemos preservar medi��es a 14-12-23 estamos a considerar que ditas medi��es s�o apagadas quando se apaga a respetiva esta��o
DELETE FROM Medicoes 
WHERE IDS = 1
DELETE FROM Lugar 
WHERE IDE = 1

ALTER INDEX indexE ON Estacoes REBUILD;
ALTER INDEX indexS ON Sensor REBUILD;
ALTER INDEX indexL ON Lugar REBUILD;
ALTER INDEX indexM ON Medicoes REBUILD;

--TRUNCATE TABLE Sensor;
--TRUNCATE TABLE Medicoes;
--TRUNCATE TABLE Estacoes;
--TRUNCATE TABLE Lugar;