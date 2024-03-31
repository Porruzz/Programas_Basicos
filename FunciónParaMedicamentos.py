def mensaje_medicamentos(opcion):
    print("Buenas Tardes Señor Usuario")
    print("Elegiste la opcion: " +  str(opcion))

opcion = int(input("Ingrese una opción\n - Analgésicos \n - Antibióticos\n - Antidepresivos \n(1, 2, 3): "))

if opcion == 1:
    mensaje_medicamentos("Dirigase Por Favor A La Caja 3")
elif opcion == 2:
    mensaje_medicamentos("Dirigase Por Favor A La Caja 1")
elif opcion == 3:
    mensaje_medicamentos("Dirigase Por Favor A La Caja 2")
else:
    print("Opción Incorrecta Vuelve A Intentarlo")
