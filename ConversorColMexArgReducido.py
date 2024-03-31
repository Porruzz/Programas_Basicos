# Menú
menu = """
1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opción: """

# Función para convertir pesos a dólares
def cambio_dinero(pesos, valor):
    pesos = float(input(f"Cuántos pesos {pesos} quieres cambiar a dólares?: "))
    valor_dolar = valor
    dolares_totales = pesos / valor_dolar
    dolares_totales = round(dolares_totales, 2)
    dolares_totales = str(dolares_totales)
    print(f"Su total de dólares son {dolares_totales}$")

# Bienvenida
print("=" * 20)
print("Bienvenido al conversor de monedas")
print("=" * 20)

# Opción del usuario
opcion = int(input(menu))

# Conversión según la opción
if opcion == 1:
    cambio_dinero("colombianos", 4605)
elif opcion == 2:
    cambio_dinero("argentinos", 70)
elif opcion == 3:
    cambio_dinero("mexicanos", 22)
else:
    print("Por favor escoge un número del menú")
