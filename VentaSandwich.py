import time;

#Declarar variables y constantes
precioChurrasco=1500;
precioCompleto=1000;
precioVegetariano=2000;
precioBarrosLucos=3000;
totalCompra=0;
cantidadChurrascos=0;
cantidadCompletos=0;
cantidadVegetarianos=0;
cantidadBarrosLuco=0;
descuento=0.1;
respuesta="";
codigoH="xxhunter";

#Mostrar los precios
print("\nBienvenida/o a la Sandwicheria Trata de Agradarme\n");
time.sleep(2);
print("Lista de Precios\n");
time.sleep(2);
print("1.- Churrascos ----$1.500\n2.- Completos ----$1.000\n3.- Vegetarianos ----$2.000\n4.- Barros Luco ----$3.000\n");

#Solicitar la cantidad de cada tipo
cantidadChurrascos=int(input("¿Cuántos churrascos quiere? "));
cantidadCompletos=int(input("¿Cuántos completos quiere? "));
cantidadVegetarianos=int(input("¿Cuántos vegetarianos quiere? "));
cantidadBarrosLuco=int(input("¿Cuántos barros luco quiere? "));

#Calcular el total a pagar
totalCompra=totalCompra+(cantidadChurrascos*precioChurrasco);
totalCompra=totalCompra+(cantidadCompletos*precioCompleto);
totalCompra=totalCompra+(cantidadVegetarianos*precioVegetariano);
totalCompra=totalCompra+(cantidadBarrosLuco*precioBarrosLucos);

#Mostrar el total de la compra
print(f"El total de la compra es ${totalCompra}\n");

#Ahora viene el descuento y la validación
respuesta=input("¿Tiene un cupón de descuento? (Si/No)");

if (respuesta=="si"):
    codigo=input("Ingrese el código de descuento: ");
    if (codigo==codigoH):
        totalCompra=totalCompra-(totalCompra*descuento);
        print("Usted tiene un descuento del 10%");
        print(f"El total de compra con descuento es ${totalCompra}");
    else:
        print("Código incorrecto");
elif (respuesta=="no"):
    print("Usted no tiene descuento.");
    print(f"El total de la compra es ${totalCompra}\n");
else:
    print("Se equivocoooooooooooooooo. Vuelva a intentarlo.");

print("\nGracias por su compra. Disfrute su comida....\n");



