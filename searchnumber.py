try:
    numberlist=[]
    for i in range(0,5):
        numberlist.append(int(input("ingrese numero entero: ")))
except ValueError:
    print("ingresaste un digito invalido me mori")
else:
    try:
        useri=int(input("ingresa un elemento: "))
    except:
        print("ingresaste un valor no valido, solo numero enteros por favor ")
    else:

        if useri in numberlist:
            print("si existe")
        
        if useri not in numberlist:
            print("no existe")