BEGIN TRAN
CREATE TABLE Estacoes
(
  IDE INT IDENTITY(1,1) PRIMARY KEY ,
  Tipo_Movilidade NVARCHAR(6) NOT NULL CHECK (Tipo_Movilidade IN ('movel','fixa')), 
  DataInstalacao DATE NOT NULL,
  NumSensores INT NOT NULL CHECK (NumSensores IN (1,2)),
  Frequencia INT NOT NULL 
);  
COMMIT;

BEGIN TRAN
CREATE TABLE Sensor
(
  IDS INT IDENTITY(1,1) PRIMARY KEY ,
  Tipo_sensor NVARCHAR(20) NOT NULL CHECK (Tipo_sensor IN ('70013A GM','70018A GM')) ,
  Nivel_Medicoes INT NOT NULL,
  Nome NVARCHAR(5) NOT NULL CHECK (Nome IN ('MIRA', 'TUNA')),
  Marca NVARCHAR(8) NOT NULL CHECK (Marca = 'Envinet'),
  IDE INT NOT NULL CHECK (IDE > 0),
  FOREIGN KEY (IDE) REFERENCES Estacoes(IDE)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);
COMMIT;

BEGIN TRAN
CREATE TABLE Lugar
(
  IDL INT IDENTITY(1,1) PRIMARY KEY,
  Distrito NVARCHAR(20) NOT NULL,
  NivelMedio FLOAT NULL ,
  CoordX FLOAT NOT NULL,
  CoordY FLOAT NOT NULL,
  IDE INT NOT NULL CHECK (IDE > 0),
  FOREIGN KEY (IDE) REFERENCES Estacoes(IDE)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);
COMMIT;


BEGIN TRAN
CREATE TABLE Medicoes
(
  IDM INT IDENTITY(1,1) PRIMARY KEY,
  DataMedicao DATE NOT NULL,
  RadLevel FLOAT NULL CHECK (RadLevel BETWEEN 0 AND 10000000000),
  NivelAlerta INT  NULL CHECK (NivelAlerta IN (1,2,3,4,5)),
  IDS INT NOT NULL CHECK (IDS > 0),
  IDL INT NOT NULL CHECK (IDL > 0),
  FOREIGN KEY (IDS) REFERENCES Sensor(IDS)
  ON UPDATE CASCADE
  ON DELETE CASCADE,
  FOREIGN KEY (IDL) REFERENCES Lugar(IDL)
);

COMMIT;


CREATE UNIQUE INDEX indexE ON Estacoes(IDE);
CREATE UNIQUE INDEX indexS ON Sensor(IDS);
CREATE UNIQUE INDEX indexL ON Lugar(IDL);
CREATE UNIQUE INDEX indexM ON Medicoes(IDM);

CREATE TABLE Valoresv2 (
Abrantes NVARCHAR(50),
Abrantes_Pego NVARCHAR(50),
Beja NVARCHAR(50),
Braganca NVARCHAR(50),
Canas_de_Senhorio NVARCHAR(50),
Castelo_Branco NVARCHAR(50),
Coimbra NVARCHAR(50),
Cunha_Baixa NVARCHAR(50),
Elvas NVARCHAR(50),
Evora NVARCHAR(50),
Faro NVARCHAR(50),
Fratel_estacao_submersa NVARCHAR(50),
Funchal NVARCHAR(50),
Junqueira NVARCHAR(50),
Juromenha_estacao_submersa NVARCHAR(50),
Lisboa NVARCHAR(50),
Meimoa NVARCHAR(50),
Mesquitela NVARCHAR(50),
Penhas_Douradas NVARCHAR(50),
Pocinho_estacao_submersa NVARCHAR(50),
Ponta_Delgada NVARCHAR(50),
Portalegre NVARCHAR(50),
Porto NVARCHAR(50),
Reboleiro NVARCHAR(50),
Sines NVARCHAR(50),
Vila_Real NVARCHAR(50)
);