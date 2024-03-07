import pyodbc
import csv
import datetime

# Connection details
server = '192.168.100.14'
database = 'BD_PL2_06'
username = 'User_BD_PL2_06'
password = 'diubi:2023!BD!PL2_06'

mediaAbrantes = 34.65
mediaAbrantesPego = 72.34
mediaBeja = 22.87
mediaBraganca = 28.66
mediaCanas = 185.63
mediaCB = 98.81
mediaCoimbra = 68.06
mediaCunha = 278.78
mediaElvas = 84.42
mediaEvora = 40.31
mediaFaro = 25.54
mediaFratel = 8.13
mediaFunchal = 40.19
mediaJunqueira = 76.27
mediaJuromenha = 35.10
mediaLisboa = 60.4
mediaMeimoa = 82.41
mediaMesquitela = 224.8
mediaPenhas = 135.63
mediaPocinho = 22.63
mediaPontaDelgada = 83.94
mediaPortalegre = 95.17
mediaPorto = 126.69
mediaReboleiro = 305.94
mediaSines = 40.04
mediaVilaReal = 154.86

medias = {
     1 : mediaAbrantes ,
     2 : mediaAbrantesPego ,
     3 : mediaBeja ,
     4 :  mediaBraganca,
     5 :  mediaCanas,
     6 : mediaCB,
     7 : mediaCoimbra,
     8 : mediaCunha,
     9 : mediaElvas,
     10 : mediaEvora,
    11 : mediaFaro,
    12 : mediaFratel,
    13 : mediaFunchal,
    14 : mediaJunqueira,
    15 : mediaJuromenha,
    16 : mediaLisboa,
    17 : mediaMeimoa,
    18 : mediaMesquitela,
    19 : mediaPenhas,
    20 : mediaPocinho,
    21 : mediaPontaDelgada,
    22 : mediaPortalegre,
    23 : mediaPorto,
    24 : mediaReboleiro,
    25 : mediaSines,
    26 : mediaVilaReal,
}

def nivel_alerta(media, valor):
    if valor < media:
        return 0
    elif valor <= 1.05 * media:
        return 1
    elif valor <= 1.15 * media:
        return 2
    elif valor <= 1.05 * media:
        return 1
    elif valor <= 1.25 * media:
        return 3
    elif valor <= 1.35 * media:
        return 4
    elif valor <= 1.45 * media:
        return 5
    elif valor <= 1.65 * media:
        return 6
    elif valor > 1.65 * media:
        return 7
# Create a connection string
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Attempt to establish a connection
    connection = pyodbc.connect(connection_string)

    # If successful, create a cursor to execute SQL queries
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    cursor.execute('SELECT * FROM Medicao')

    for row in cursor.fetchall():
        idm = row[0]
        data = row[1]
        radiacao = row[2]
        ids = row[3]
        cursor2.execute('SELECT Lugar.IDL FROM Lugar INNER JOIN Sensor ON Sensor.IDL = Lugar.IDL WHERE Sensor.IDS = ?',ids)
        idl = None
        for row2 in cursor2.fetchall():
            idl = row2[0]
        alerta = nivel_alerta(radiacao, medias[idl])
        cursor.execute('INSERT INTO Alerta(Datas,IDM,IDL,Alerta) VALUES(?, ?, ?, ?)', data, idm, idl, alerta)
    cursor.commit()
    
    # Execute a SQL query to select all records from the "Estacoes" table
    
    # Fetch all rows from the result set
    #rows = cursor.fetchall()

    # Print column names
    #print([column[0] for column in cursor.description])

    # Print the data
    #for row in rows:
    #    print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()  
except pyodbc.Error as e:
    # If there's an error, print the error message
    print(f"Connection failed. Error: {e}")