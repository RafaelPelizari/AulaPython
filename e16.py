# criar um vetor que insira 6 nomes e imprima
notas = [0.0]*6
print(notas)
print('digite 6 notas:')
for i in range(6):
    notas[i] = input(float())
    print(notas)
