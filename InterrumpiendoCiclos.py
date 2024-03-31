def run():
    # Imprime Todos Los Números Pares
    for contador in range(1000):
        if contador %  2 != 0:
            continue
        print(contador)

    # Imprimer Los Numeros Del 0 al 10000 Pero Termina en 5678
    for i in range(10000):
        print(i)
        if i == 5678:
            break
    
    # Imprime los caracteres pero para la ejecución con el caracter "o"
    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)



if __name__ == "__main__":
    run()