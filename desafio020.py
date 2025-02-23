import random 

# Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio 
# chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 
# 12 para compor a salada de frutas da pessoa cliente.

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada_de_frutas = random.sample(frutas, 3)

print(f'Sua salada de frutas será de: {salada_de_frutas}')

