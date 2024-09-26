def calcula():
    numeroum = int(input('Digite um número: '))
    numerodois = int(input('Digite mais um número: '))


    soma = numeroum + numerodois
    subtracao = numeroum - numerodois 
    multiplicacao = numeroum * numerodois
    divisao = numeroum / numerodois
    expo = numeroum ** numerodois

    print(f"""
        Soma = {soma}
        Subtração = {subtracao}
        Multiplicação = {multiplicacao}
        Divisão = {divisao}
        Exponenciação = {expo}
        """)
    

calcula()