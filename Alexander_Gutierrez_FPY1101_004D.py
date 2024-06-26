lista_estudiante=[]
#Crear menu
while True:
        print("1.- Agregar estudiante")
        print("2.- ver todos los estudiantes")
        print("3.- modificar un estudiante")
        print("4.- eliminar estudiante")
        print("5.- guardar coleccion de un archivo")
        print("6.- salir del programa")
#opciones
        opcion=input("Ingrese su opcion: ")
        if opcion=="1":
            estudiante=input("Ingrese el estudiante:")
            edad=input("Ingrese la edad de estudiante:")
            curso=input("Ingrese el curso del estudiante:")
            promedio=input("Ingrese el promedio del estudiante:")
            print("Se agrego correctamente a la lista")
            lista_estudiante.append([estudiante,edad,curso,promedio])
        elif opcion=="2":
              """print(f"esta es la lista de estudiantes ingresado: {lista_estudiante}")
              print("--------------------------------------")
              print("|    Nombre         | Edad | Curso | Promedio |")
              print(f"| {estudiante}       {edad}   {curso}     {promedio}|")"""  
              for estudiante in lista_estudiante:
                   print(f"Estudiante: {estudiante[0]}, Edad {estudiante[1]}, Curso {estudiante[2]}, Promedio {estudiante[3]}")
        elif opcion=="3":
              modificar=input("ingrese el valor que desea modificar:")
              lista_estudiante.reverse(modificar)
        elif opcion=="4":
             estudiante=input("Ingrese la opcion ingresada que desea eliminar:")
             for estudiante in lista_estudiante:
                  if estudiante[0]== estudiante:
                   lista_estudiante.remove(estudiante)
                   print("Se Borro corectamente")
        elif opcion=="5":
             print("Su coleccion se agrego en un archivo")
             with open("estudiantes.txt", 'w', encoding= "utf-8") as archivo:
                  archivo.write (f"{lista_estudiante}")
        elif opcion=="6":
             print("Saliendo del programa,vuelva pronto")
             break
        else:
             print("Error vuelva a intentarlo")
                  
                  
        

