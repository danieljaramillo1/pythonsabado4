import math
choise =100
number = int(input("ingresa el numero natural: "))
print(f" ")
print(f". ")
print("0. PARA SALIR")
print("1. PARA SABER SI ES MULTIPLO DE 2")
print("2. PARA RAIZ CUADRADA")
print("3. SUMAR 100")
print("4. ELEVAR AL CUADRADO")
print(f" ")
print(f". ")
while choise != 0:

    try:
       
        choise = int(input("que quieres hacer: "))
    except:
        print("INGRESASTE UN VALOR ERRONEO DEBE SER UN NUMERO NATURAL")
    else:
        if choise == 0:
            print("se acabo")
            break

        elif choise == 1:
            if number%2 == 0:
                print("el numero es multiplo de 2")
            else:
                print("el numero no es multiplo de 2")
        elif choise == 2:
            number = math.sqrt(number)
            print(number)
        elif choise == 3:
            number= number + 100
            print(number)
        elif choise == 4:
            number = number * number
            print(number)
        else:
            print("seleccionaste ua opcion invalida")
            
        


        
    




