
#TITULO
print("Te mostrare la estacion dependiendo del dia y mes: ")

##CREO UN CALENDARIO
calendar=(
('diciembre','enero','febrero','marzo','12','1','2','3'),
('marzo','abril','mayo','junio','3','4','5','6'),
('junio','julio','agosto','septiembre','6','7','8','9'),
 ('septiembre','octubre','noviembre','diciembre','9','10','11','12')
       )    
##menu
winter=0
summer =1
fall = 2
spring =3
print(calendar)
print('1' in calendar)

day = int(input("ingrese el Día: "))
print("para el mes puedes usar letras o numeros ")
monthx = (input("ingrese el Mes: "))
month = monthx.lower()
print(f'fecha seleccionada: {day}/{month}/2022')



            



