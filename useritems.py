try:
    size = int(input("Dame el tamaño: "))
except ValueError:
    print("ingresa un numero entero por favor")
else:
    
    items=[]
    if(size!=0):

        for i in range(0,size):
            items.append(input("ingresa un valor: "))
        print(items)
                
    else:
        print("ingresaste cero idiot")