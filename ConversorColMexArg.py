# Menú de opciones
menu = """
Bienvenido al conversor de monedas

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opción: """

# Entrada de la opción del usuario
opcion = int(input(menu))

# Conversión de pesos colombianos a dólares
if opcion == 1:
    pesos_colombianos = int(input("¿Cuántos pesos colombianos quieres cambiar a dólares?: "))
    pesos_colombianos = float(pesos_colombianos)
    valor_dolar = 4605
    dolares_totales = pesos_colombianos / valor_dolar
    dolares_totales = round(dolares_totales, 2)
    dolares_totales = str(dolares_totales)
    print(f"Su total de dólares son {dolares_totales} $")

# Conversión de pesos argentinos a dólares
elif opcion == 2:
    pesos_argentinos = int(input("¿Cuántos pesos argentinos quieres cambiar a dólares?: "))
    pesos_argentinos = float(pesos_argentinos)
    valor_dolar = 65
    dolares_totales = pesos_argentinos / valor_dolar
    dolares_totales = round(dolares_totales, 2)
    dolares_totales = str(dolares_totales)

    print(f"Su total de dólares son {dolares_totales} $")

# Conversión de pesos mexicanos a dólares
elif opcion == 3:
    pesos_mexicanos = int(input("¿Cuántos pesos mexicanos quieres cambiar a dólares?: "))
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar = 24
    dolares_totales = pesos_mexicanos / valor_dolar
    dolares_totales = round(dolares_totales, 2)
    dolares_totales = str(dolares_totales)
    print(f"Su total de dólares son {dolares_totales} $")

# Mensaje de error
else:
    print("Por favor, elige una opción válida (1, 2 o 3)")
