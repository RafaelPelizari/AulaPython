maioralt=0
menoralt=4
maiorpeso=0
menorpeso=600
rep=5
for cont in range(rep):
    peso = float(input("peso:"))
    altura = float(input("altura:"))
if(altura>maioralt):
        maioralt=altura
if(altura<menoralt):
        menoralt=altura
if(peso>maiorpeso):
        maiorpeso=peso
if(peso<menorpeso):
         menorpeso=peso
print("maior altura:", maioralt)
print("menor altura:",menoralt)
print("maior peso:",menorpeso)
print("menor peso:",menorpeso)


