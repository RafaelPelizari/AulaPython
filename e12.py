print("calcular imc. peso/alt*altura/n")
for cont in range (1,5):
    altura= float(input("Altura:"))
    peso=float(input("peso:"))
    imc=peso/(altura*altura)
    print("imc:",imc)
    if (imc>=40):
        print("obesidade 3")
    elif (imc>=35):
        print("obsidade")
    elif (imc>=30):
        print("obesidade")
    elif(imc>=25):
        print("sobrepeso") 
    elif(imc>18.5):
        print("peso normal")
    elif(imc<18.5):
        print("abaixo do peso normal")   
