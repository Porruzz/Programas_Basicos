# Función De Promedio
def calcular_promedio(num1, num2):
    return (num1 + num2) / 2

# Pedir Notas Al Usuario
def get_user_input():
    grade1 = float(input("Enter the grade for the first subject: "))
    grade2 = float(input("Enter the grade for the second subject: "))
    grade3 = float(input("Enter the grade for the third subject: "))
    return grade1, grade2, grade3

# Datos de Usuario
grades = get_user_input()

# Calcular Promedio
average = calcular_promedio(grades[0], calcular_promedio(grades[1], grades[2]))

# Comprobación De Aprobado O No Aprobado
if average >= 3.0:
    print("The student passed the course with an average of:", average)
else:
    print("The student failed the course with an average of:", average)