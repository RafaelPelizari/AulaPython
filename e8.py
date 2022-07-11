print("reajuste salarial")
salario = float(input("salario:"))
if (salario>1000):
    salnovo = salario+(salario*0.05)
if(salario>=500):
    salnovo = salario+(salario*0.10)
elif(salario<500):
     salvnovo = salario+(salario*0.15)
print("salario novo:",salnovo)