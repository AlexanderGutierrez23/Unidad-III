#Crear una lista de trabajadores en una matriz
import csv
matriz=[
  ['Nombre','Cargo','Sueldo']
]
listanombre=[]
listacargo=[]
listasueldo=[]

for i in range(3):
 nombre=input("Ingrese el nombre del trabajador Y su appelido:")
 cargo=input("Ingrese su cargo correspondiente:")
 Sueldo=input("Ingrese su sueldo bruto:")
 listanombre.append(nombre)
 listacargo.append(cargo)
 listasueldo.append(Sueldo)

#Crear el contexto para abrir un nuevo archivo.csv
with open('trabajo/archivo_trabajadores.csv', 'w' , newline='', encoding='utf-8') as archivo_csv:
  escritor_csv= csv.writer(archivo_csv)
print("El archivo se creo correctamente")
#ir a la fila en el arvhivo csv
escritor_csv.writerows(matriz)
#escribir multiples filas en el archivo csv
escritor_csv.writerows(listacargo)
print("El archivo se creo correctamente")

#leer archivo.csv
import csv
with open ('trabajo/archivo_trabajadores.csv', 'r' , newline='', encoding='utf-8') as archivo_csv:
  lector_csv=csv.reader(archivo_csv)
  for x in lector_csv:
   print(x)

