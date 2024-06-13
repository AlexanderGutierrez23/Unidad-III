#Funciones en python

#Función sumar dos número con parametros y con retorno
def sumarDosNumeros(num1,num2):
    suma=(num1+num2);
    print(f"La suma es: {suma}");

#Función restar dos número con parametros y con retorno
def restarDosNumeros(num1,num2):
    resta=(num1-num2);
    print(f"La resta es: {resta}")

#Función multiplicar dos número con parametros y con retorno
def multiplicarDosNumeros(num1,num2):
    multiplicacion=(num1*num2);
    return multiplicacion;

#Función dividir dos número con parametros y con retorno
def dividirDosNumeros(num1,num2):
    division=(num1/num2);
    return division;


#Crear un sistema de Administración de Productos de una Ferreteria
#Función para agregar productos.
#Función para mostrar productos.
#Función para buscar productos.
#Función para eliminar productos.

listaProductos=["Hacha","Pala","Carretilla","Guantes"];

def agregarProductos():
    producto=input("Ingrese el nuevo producto --> ");
    if buscarProducto(producto)==False:
        listaProductos.append(producto);
        print("Se ingreso el producto correctamente.");
    else:
        print("El producto ya se encuentra en la lista.")

def mostrarProductos():
    print(listaProductos);
    for i in range(len(listaProductos)):
        print(f"{i+1}.- {listaProductos[i]}");

def buscarProducto(producto):
    if producto in listaProductos:
        print("El producto está en la lista.");
        return True;
    else:
        print("El producto NO está en la lista.");
        return False;

def eliminarProducto():
    producto=input("Ingrese el producto que desea eliminar: ");
    if (buscarProducto(producto)==True):
        listaProductos.remove(producto);
        print("El producto se eliminó correctamente.");
    else:
        print("El producto no se eliminó.");


