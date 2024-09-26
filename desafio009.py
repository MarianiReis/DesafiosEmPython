def imprimelista():
    frutas = ['banana', 'maçã', 'uva', 'manga']

    frutas.remove('manga')
    del frutas[-1]
    
    print(frutas)

imprimelista()