#Conexion a BD SQL
import pyodbc

server = '10.20.14.15'
bd = 'DS_PREVFRAUD'
usuario = 'hsantos'
contrasena = 'Sevass2023a'

conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server + ';DATABASE='+ bd +'; UID=' + usuario + '; PWD='+contrasena)


 #Consulta a la base de datos
cursor =  conexion.cursor()
# cursor.execute("Drop Table IF Exists dbo.Jsondemo Create Table dbo.Jsondemo (jsondata varchar(max))")
# cursor.execute("Drop Table IF Exists dbo.Jsondemo Create Table dbo.Jsondemo (jsondata varchar(max))")
cursor.execute("Select name From master.sys.databases Order by 1 " + 
               "For JSON PATH , ROOT('Linea'); ")

tarea = cursor.fetchone()
while tarea:
    print(tarea[0])
    tarea = cursor.fetchone()

tareas = cursor.fetchall()

for tarea in tareas:
     print(tarea)
cursor.close()
conexion.close()