print('leia 3 nomes, sexo, altura de 3 pesssoas')
repeticoes = 3
for contador in range(repeticoes):
    nome = input("nome:")
    sexo = input("sexo:")
    altura = float(input("altura:"))
    if (sexo=="f"):
        print('feminino')
    elif(sexo=="m"):
        print("masculino")
        print("nome")
