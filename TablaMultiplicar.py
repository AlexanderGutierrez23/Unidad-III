#Declarar variables

num=0;
rango=range(1,11);
resultado=0;

#Ingresar número
num=int(input("Ingrese un número señor/a: "));
print(f"Tabla del {num}\n");

#Ciclo FOR
for i in rango:
    resultado=num*i;
    print(f"{num} X {i} = {resultado}");

#Ciclo WHILE
print("Ciclo WHILE\n");
i=1;
while (i<11):
    resultado=num*i;
    print(f"{num} X {i} = {resultado}");
    i=i+1;



