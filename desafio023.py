#Escreva um programa que pergunte salário do funcionario e calcule o valor do aumento. Para salarios superiores a 
# R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15%.


salario = float(input('Digite o seu salário: '))

print(
    """Seu salário se encaixa em quais das opções abaixo:
     
     (1) Acima de R$ 1.250,00
     (2) Abaixo ou igual a R$1.250,00

    """
    )

opcao = int(input('Digite uma opção: '))

if opcao == 1:
    aumento = salario / 10 * 100
    print(f'O seu aumento foi de: {aumento}')
elif opcao == 2:
    aumento = salario / 15 * 100
    print(f'O seu aumento foi de: {aumento}')
else:
    print('Opção inválida')