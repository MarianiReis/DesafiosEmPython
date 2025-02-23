from random import choice


while True:

    try:
        
        participantes_sorteio = input('Digite o número de participantes: ')
        if participantes_sorteio.isdigit():
            participantes_sorteio = int(participantes_sorteio)
            break
        else:
            print("Número inválido, tente novamente. Exemplos corretos: 30, 12, 43, etc ")
    except ValueError:
        print('O número digitado é inválido. Digite um número inteiro.')
     
    

lista_de_sorteio = []

for i in range(1, participantes_sorteio + 1):
    lista_de_sorteio.append(i) 

numero_sorteado = choice(lista_de_sorteio)

print(f'O número sorteado é: {numero_sorteado}')