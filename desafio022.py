#escreva um programa que leia três números e imprima o maior e o menor

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

numeros = (numero1, numero2, numero3)

valor_maximo = max(numeros)
valor_minimo = min(numeros)

print(f'O maior número é {valor_maximo}, o menor número é {valor_minimo}')