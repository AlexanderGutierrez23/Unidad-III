#Juego de azar
import random;
import time;

lista_numeros=[];

print("\nBienvenido a Loteria Hettel\n");
print("Ingrese sus 5 números de la suerte.");

for i in range(5):
    num=int(input("Ingrese número: "));
    lista_numeros.append(num);

print(f"Sus números de la suerte son: {lista_numeros}\n");

lista_aleatoria=[];

for i in range(5):
    while True:
        num_aleatorio=random.randint(1,11);
        time.sleep(2);
        print(f"El número generado es: {num_aleatorio}");
        if num_aleatorio not in lista_aleatoria:
            lista_aleatoria.append(num_aleatorio);
            break;

print(f"La lista generada es: {lista_aleatoria}");

contador=0;

for x in lista_numeros:
    if x in lista_aleatoria:
        contador=contador+1;
        print(f"Acertó en el número {x}");

if contador==5:
    print("GANASTE TU PREMIO. ¡¡¡FELICIDADES!!!");
else:
    print("Suerte la próxima vez.")

