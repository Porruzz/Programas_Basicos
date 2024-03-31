def convert_units():
    print("Conversor De Unidades \n1 - Libras a Kilos\n2 - Kilos a Libras\n3 - Euros a Dolares\n4 - Dolares a Euros")
    opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
    result = 0

    if opcion == 1:
        print("Libras a Kilos")
        entrada = float(input("Ingresa la cantidad en Libras: "))
        result = round(entrada*0.453592,2)
    elif opcion == 2:
        print("Kilos a Libras")
        entrada = float(input("Ingresa la cantidad en Kilogramos: "))
        result = round(entrada*2.20462,2)
    elif opcion == 3:
        print("Euros a Dolares")
        entrada = float(input("Ingresa la cantidad en Euros: "))
        result = round(entrada*1.19,2)
    elif opcion == 4:
        print("Dolares a Euros")
        entrada = float(input("Ingresa la cantidad en Dolares: "))
        result = round(entrada*0.84,2)
    else:
        print("Opción inválida. Inténtelo nuevamente.")
        convert_units()

    print("El resultado de la conversión es: {} ".format(result))

convert_units()
