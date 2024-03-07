
DELETE FROM Estacoes 
WHERE IDE = 2
DELETE FROM Sensor 
WHERE IDE = 1
-- ver se ao apagar estações podemos preservar medições a 14-12-23 estamos a considerar que ditas medições são apagadas quando se apaga a respetiva estação
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