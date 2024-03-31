def convert_units():
    print("Conversor De Pesos Colombianos \n1 - Dolares \n2 - Euro \n3 - Cake \n4 - Bitcoin")
    opcion = int(input("Ingrese el numero de la opción de conversión que desea utilizar: "))
    result = 0

    if opcion == 1:
        print("Dolares")
        entrada = float(input("Cuanto Desea Convertir?: $"))
        result = round(float(entrada*3679), 2)
    elif opcion == 2:
        print("Euro")
        entrada = float(input("Cuanto Desea Convertir?: $"))
        result = round(float(entrada*4383), 2)
    elif opcion == 3:
        print("Cake")
        entrada = float(input("Cuanto Desea Convertir?: $"))
        result = round(float(entrada*58800), 2)
    elif opcion == 4:
        print("Bitcoin")
        entrada = float(input("Cuanto Desea Convertir?: $"))
        result = round(float(entrada*136134100), 2)
    else:
        print("Opción inválida. Inténtelo nuevamente.")
        convert_units()

    print("El resultado de la conversión es: $ {} ".format(result))

convert_units()