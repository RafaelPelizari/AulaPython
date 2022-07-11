print("número positivo,negatico,neutro/n")
for num in range(1,4):
    num = int(input("Número:"))
    if (num >0):
        print(num,"positivo")
    elif (num <0):
        print(num,"negativo")
    elif(num == 0):
        print(num,"Neutro")



