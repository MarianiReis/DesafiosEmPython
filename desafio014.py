def percorrelista():
    numero = 1

    while numero <= 10:
        print(numero)
        numero = numero + 1
        if numero == 5:
            break

    while numero <= 10:
        print(numero)
        numero = numero + 1
        if numero == 5:
            continue  

percorrelista()