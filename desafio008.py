def imprimelista():
    frutas = ['banana', 'maçã', 'uva', 'manga']

    frutas.pop(0)
    frutas.insert(0, 'morango')
    frutas.append('abacaxi')

    print(frutas)

imprimelista()