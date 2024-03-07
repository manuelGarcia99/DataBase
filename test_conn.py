import pyodbc
import csv
import datetime

from pytz import timezone

# Connection details
server = '192.168.100.14'
database = 'BD_PL2_06'
username = 'User_BD_PL2_06'
password = 'diubi:2023!BD!PL2_06'




# Create a connection string
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Attempt to establish a connection
    connection = pyodbc.connect(connection_string)

    # If successful, create a cursor to execute SQL queries
    cursor = connection.cursor()

    csv_file_path = 'C:/Users/manec/Desktop/Base de Dados/GS2.csv'
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')

        header = next(csv_reader)

        table_name = "Medicao"

        for row in csv_reader:#as e 15 fazemos control c
            datas_str = row[0]
            datas_datetime_naive = datetime.datetime.strptime(datas_str, '%m/%d/%y %H:%M')#tenta sem timezone
            tz = timezone('UTC')
            datas_datetime = datas_datetime_naive.replace(tzinfo=tz)
            column1_value = datas_datetime
            column2_value = row[1]
            column3_value = row[2]
            column4_value = row[3]
            column5_value = row[4]
            column6_value = row[5]
            column7_value = row[6]
            column8_value = row[7]
            column9_value = row[8]
            column10_value = row[9]
            column11_value = row[10]
            column12_value = row[11]
            column13_value = row[12]
            column14_value = row[13]
            column15_value = row[14]
            column16_value = row[15]
            column17_value = row[16]
            column18_value = row[17]
            column19_value = row[18]
            column20_value = row[19]
            column21_value = row[20]
            column22_value = row[21]
            column23_value = row[22]
            column24_value = row[23]
            column25_value = row[24]
            column26_value = row[25]
            column27_value = row[26]



            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,1)"

            cursor.execute(insert_query, column1_value, column2_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,2)"

            cursor.execute(insert_query, column1_value, column3_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,3)"

            cursor.execute(insert_query, column1_value, column4_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,4)"

            cursor.execute(insert_query, column1_value, column5_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,5)"

            cursor.execute(insert_query, column1_value, column6_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,6)"

            cursor.execute(insert_query, column1_value, column7_value)
            
            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,7)"

            cursor.execute(insert_query, column1_value, column8_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,9)"

            cursor.execute(insert_query, column1_value, column10_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,10)"

            cursor.execute(insert_query, column1_value, column11_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,11)"

            cursor.execute(insert_query, column1_value, column12_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,12)"

            cursor.execute(insert_query, column1_value, column13_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,13)"

            cursor.execute(insert_query, column1_value, column14_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,14)"

            cursor.execute(insert_query, column1_value, column15_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,15)"

            cursor.execute(insert_query, column1_value, column16_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,16)"

            cursor.execute(insert_query, column1_value, column17_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,17)"

            cursor.execute(insert_query, column1_value, column18_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,18)"

            cursor.execute(insert_query, column1_value, column19_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,19)"

            cursor.execute(insert_query, column1_value, column20_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,20)"

            cursor.execute(insert_query, column1_value, column21_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,21)"

            cursor.execute(insert_query, column1_value, column22_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,22)"

            cursor.execute(insert_query, column1_value, column23_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,23)"

            cursor.execute(insert_query, column1_value, column24_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,24)"

            cursor.execute(insert_query, column1_value, column25_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,25)"

            cursor.execute(insert_query, column1_value, column26_value)

            insert_query = f"INSERT INTO Medicao(Datas, Radiacao, IDS) VALUES (CONVERT(DATETIME, ?, 16),?,26)"

            cursor.execute(insert_query, column1_value, column27_value)
        connection.commit()

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