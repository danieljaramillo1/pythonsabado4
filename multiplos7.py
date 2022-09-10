
try:
    size = int(input("Dame el tamaño: "))
except ValueError:
    print("ingresa un numero entero por favor")
else:
    i=1
    multiplos=[]
    if(size!=0):

        for i in range(1,size+1):
            multiplos.append(i*7)
        print(multiplos)
            
        
    else:
        print("ingresaste cero idiot")
        
    


    
