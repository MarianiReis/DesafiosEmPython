#Trabalhando com filas em python


ultimo = 10 

fila = list(range(1, ultimo + 1))

while True:

    print(f"Existem {len(fila)} clientes na fila ")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("Ou A para realizar o atendimento. S para sair.")

    operacao = input("Operação (F, A, ou S): ")
    lista_operacao = list(operacao)


    for i in lista_operacao:
        if i == "A": 
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido. ")
            else: 
                print("Fila vazia! Ninguém para atender.")
        elif i == "F": 
            ultimo += 1
            fila.append(ultimo)
        elif i == "S":
            break
        else: 
            print("Operação inválida! Digite apenas F, A, ou S")



