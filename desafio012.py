def percorrelistasaninhadas():
    lista = []
    for x in [1,2,3,4]:
        for y in [2,5,6,7]:
            if x != y:
                lista.append((x, y))

    print(lista)


percorrelistasaninhadas()