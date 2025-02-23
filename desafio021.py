#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem 
# dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5,00 po km acima de 80km/h



velocidade = int(input('velocidade do automóvel: '))

multa_por_quilometro = 5

if velocidade > 80:
    valor_da_multa = (velocidade - 80) * multa_por_quilometro
    print(f'Você foi multado, o valor da sua multa é de: R${valor_da_multa},00')
    
    
