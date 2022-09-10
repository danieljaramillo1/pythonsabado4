flag = True
suma=0
total =0
while flag == True:

    try:
        
        value=int(input("ingresa un valor a ser sumado! no puede ser negativo: ")) 
    except:
        print("debes ingresar valores enteros no negativos para seguir sumando me mori!!!")
        flag = False
        break
    else:
        if value<0:
            print("debes ingresar valores enteros no negativos para seguir sumando me mori!!!")
            flag = False
            break
        else:

            total = total+value
            print(f'el acumulado es',total)
            
