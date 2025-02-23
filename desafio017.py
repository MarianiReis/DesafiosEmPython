letra = input("Digite uma letra: ")

vogais = ('a','e','i','o','u')


if letra.lower() in vogais:
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")

