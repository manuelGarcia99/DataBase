import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import pyodbc
from datetime import datetime

# Connection details
server = 'localhost'
database = 'RADNET'
username = 'sa'
password = 'sa'


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

# Initialize the SQL Server connection
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Initialize main window
root = tk.Tk()
root.title("Database Management")

# Set the initial window size
root.geometry("1000x800")  # Adjust the size as needed

# Variable to store the current page
current_page = None

# Function to handle back button click
def back_button_clicked():
    # Switch back to the main page
    show_page("main_page")

# Function to switch to a new page
def show_page(page_name):
    global current_page
    # Remove current page if it exists
    if current_page is not None:
        current_page.grid_remove()

    # Switch to the requested page
    if page_name == "main_page":
        main_page.grid()
        current_page = main_page
    elif page_name == "operations_page":
        operations_page.grid()
        current_page = operations_page
    elif page_name == "alertas_page":
        alertas_page.grid()
        current_page = alertas_page

# Function to handle data insertion
def insert_data():
    data_value = data_entry.get()
    datas_datetime = datetime.strptime(data_value, '%m/%d/%y %H:%M')
    radiacao_value = float(radiacao_entry.get())
    nome_value = nome_entry.get()

    # Get the IDL from the Lugar table based on the Nome

        

    # Your SQL INSERT statement for Medicao table goes here
    insert_query = f"INSERT INTO Medicao (Datas, Radiacao, IDS) VALUES (?, ?, (SELECT Sensor.IDS FROM Sensor INNER JOIN Lugar ON Lugar.IDL = Sensor.IDL  WHERE   Lugar.Nome = ?))"

    try:
        # Execute the INSERT query
        cursor.execute(insert_query, datas_datetime, radiacao_value, nome_value)
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inserting data: {str(e)}")

        messagebox.showerror("Error", f"Lugar with Nome '{nome_value}' not found.")

    radDaTerra= None
    idlTerra= None
    cursorTemp = conn.cursor()
    cursorTemp = cursor.execute("SELECT TOP 1 Radiacao,IDS FROM Medicao ORDER BY IDM DESC")
    for row in cursorTemp.fetchall():
        radDaTerra = row[0]
        idlTerra = row[1]



    insert_query = f" INSERT INTO ALerta (Datas , IDM , IDL, Alerta) VALUES (?, (SELECT TOP 1 IDM FROM Medicao ORDER BY IDM DESC),(SELECT IDL FROM Lugar WHERE Lugar.Nome = ?),({nivel_alerta(medias[idlTerra],radDaTerra)}) )"
    try:
        # Execute the INSERT query
        cursor.execute(insert_query, datas_datetime,  nome_value)
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inserting data: {str(e)}")

        messagebox.showerror("Error", f"Lugar with Nome '{nome_value}' not found.")

def delete_data():
    data_value = data_entry.get()
    datas_datetime = datetime.strptime(data_value, '%m/%d/%y %H:%M')
    nome_value = nome_entry.get()

    delete_query = f"DELETE FROM Medicao WHERE Medicao.Datas = ? AND Medicao.IDS = (SELECT Sensor.IDS FROM Sensor  INNER JOIN Lugar ON Sensor.IDL = Lugar.IDL INNER JOIN Medicao Medicao2\
      ON Medicao2.IDS = Sensor.IDS WHERE ? = Medicao2.Datas AND Lugar.Nome = ?)"

    try:
        cursor.execute(delete_query,datas_datetime,datas_datetime,nome_value)
        conn.commit()
        messagebox.showinfo("Success","Data deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting data: {str(e)}")

        messagebox.showerror("Error", f"Lugar with Nome '{nome_value}' not found.")

def search_data():
    nome_value = nome_entry.get()

    search_query = f"SELECT Medicao.Radiacao, Lugar.Nome, TipoAlerta.Descricao, CAST(Medicao.Datas AS NVARCHAR(255)) AS Datas FROM Medicao INNER JOIN Alerta ON Alerta.IDM = Medicao.IDM INNER JOIN Lugar \
    ON Lugar.IDL = Alerta.IDL INNER JOIN TipoAlerta ON Alerta.Alerta = TipoAlerta.Tipo WHERE Lugar.Nome LIKE '%{nome_value}%' ORDER BY Medicao.Datas DESC"
    cursor.execute(search_query)
    grelha = Treeview(root)

    grelha['columns'] = ('Radiação','Nome do Lugar','Tipo de Alerta', 'Data')
    grelha.heading('Radiação', text='Radiação')
    grelha.column('Radiação',anchor = 'center',width = 100)
    grelha.heading('Nome do Lugar', text='Nome do Lugar')
    grelha.column('Nome do Lugar',anchor = 'center',width = 150)
    grelha.heading('Tipo de Alerta', text='Tipo de Alerta')
    grelha.column('Tipo de Alerta',anchor = 'center',width = 250)
    grelha.heading('Data', text='Data')
    grelha.column('Data',anchor = 'center',width = 200)

    
    for row in cursor.fetchall():
        grelha.insert("",tk.END, values = (row[0],row[1],row[2],row[3]))

    grelha.grid(column=0, row=0, sticky='nsew')

    

# Main Page
main_page = tk.Frame(root)

# Buttons on the main page with larger font
tk.Button(main_page, text="Operations", command=lambda: show_page("operations_page"), font=("Helvetica", 14)).pack(pady=15)
tk.Button(main_page, text="Alertas", command=lambda: show_page("alertas_page"), font=("Helvetica", 14)).pack(pady=15)

# Initial grid configuration
main_page.grid()

# Operations Page
operations_page = tk.Frame(root)

# Widgets for the Operations page with larger font
tk.Button(operations_page, text="Back", command=back_button_clicked, font=("Helvetica", 14)).pack(pady=15)

tk.Label(operations_page, text="Data:", font=("Helvetica", 12)).pack()
data_entry = tk.Entry(operations_page, font=("Helvetica", 12))
data_entry.pack()

tk.Label(operations_page, text="Radiacao:", font=("Helvetica", 12)).pack()
radiacao_entry = tk.Entry(operations_page, font=("Helvetica", 12))
radiacao_entry.pack()

tk.Label(operations_page, text="Nome:", font=("Helvetica", 12)).pack()
nome_entry = tk.Entry(operations_page, font=("Helvetica", 12))
nome_entry.pack()

tk.Button(operations_page, text="Insert", command=insert_data, font=("Helvetica", 14)).pack(pady=15)

tk.Button(operations_page, text="Delete", command=delete_data, font=("Helvetica", 14)).pack(pady=15)

tk.Button(operations_page, text="Search", command=search_data, font=("Helvetica", 14)).pack(pady=15)

# Other widgets for the Operations page go here

# Run the Tkinter event loop
root.mainloop()
