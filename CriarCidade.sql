BEGIN TRAN
INSERT INTO Estacoes(DataInstalacao,Frequencia,NumSensores,Tipo_Movilidade) VALUES('2023-12-15',ROUND(50.3,2),2,'fixa')
COMMIT;
BEGIN TRAN
INSERT INTO Sensor(Marca,Nivel_Medicoes,Nome,Tipo_Sensor,IDE) VALUES('Envinet',0,'MIRA','70018A GM',1)
COMMIT;
BEGIN TRAN
INSERT INTO Lugar(CoordX,CoordY,Distrito,NivelMedio,IDE) VALUES(28.4,12.4,'Guarda',5.5,1)
COMMIT;
BEGIN TRAN
INSERT INTO Medicoes(DataMedicao,NivelAlerta,RadLevel,IDS,IDL) VALUES('2023-12-14',5,66.5,1,1)
COMMIT;

DROP TABLE Medicoes;
DROP TABLE Lugar;
DROP TABLE Sensor;
DROP TABLE Estacoes;

BEGIN TRAN
INSERT INTO Estacoes(DataInstalacao,Frequencia,NumSensores,Tipo_Movilidade) VALUES('2023-12-16',ROUND(50.3,2),2,'fixa')
COMMIT;
BEGIN TRAN
INSERT INTO Sensor(Marca,Nivel_Medicoes,Nome,Tipo_Sensor,IDE) VALUES('Envinet',0,'MIRA','70018A GM',2)
COMMIT;
BEGIN TRAN
INSERT INTO Lugar(CoordX,CoordY,Distrito,NivelMedio,IDE) VALUES(28.4,12.4,'Coimbra',5.5,2)
COMMIT;
BEGIN TRAN
INSERT INTO Medicoes(DataMedicao,NivelAlerta,RadLevel,IDS,IDL) VALUES('2023-12-16',5,70.2,2,2)
COMMIT;