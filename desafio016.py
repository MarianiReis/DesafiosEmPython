while True:

    try: 
        percentual_primeiro_ano = input("Digite o percentual de crescimento da sua empresa do último ano: ")
        if percentual_primeiro_ano.isdigit():
                percentual_primeiro_ano = int(percentual_primeiro_ano)
                break
        else:
                print("Digite um número válido! Exemplo: 12,70,50, etc.")
    except ValueError: 
         print("Entrada inválida. Por favor digite um número inteiro.")
        

while True:

    try: 
        percentual_atual = input("Digite o percentual de crescimento da sua empresa deste ano: ")
        if percentual_atual.isdigit():
                percentual_atual = int(percentual_atual)
                break
        else:
                print("Digite um número válido! Exemplo: 12,70,50, etc.")
    except ValueError: 
        print("Entrada inválida. Por favor digite um número inteiro.")



if percentual_atual < percentual_primeiro_ano:
    print("Porcentagem negativa")
else:
    print("Porcentagem positiva")