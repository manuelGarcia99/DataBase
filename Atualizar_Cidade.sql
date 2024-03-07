BEGIN TRANSACTION
UPDATE Sensor 
SET Tipo_Sensor = 'Novo Tipo'
WHERE Sensor.IDE = 1
UPDATE Lugar 
SET CoordX = -25.8
SET CoordY = -43.4
WHERE Lugar.IDE = 1
COMMIT;

--This still needs more work but

SELECT  * FROM Estacoes;

SELECT  * FROM Medicoes;

SELECT * FROM Sensor;

SELECT * FROM Lugar;

