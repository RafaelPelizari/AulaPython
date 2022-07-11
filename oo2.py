class Funcionario:
    def __init__(self, nome: str, cpf: str, salario: float, desconto: float, salarioliquido: float):

        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.salarioliquido = salarioliquido
        self.desconto = desconto
    
    def descontar(self, salario, desconto):
        self.desconto = salario *0.05
    
    def liquidar(self, salario, desconto, salarioliquido): 
        self.salarioliquido = salario - desconto 
    
    def mostraFuncionario(self):
        print(f'nome: {self.nome}, salario: {self.salario}, cpf: {self.cpf}, salarioliquido: {self.salarioliquido}, desconto: {self.desconto}')

marcos = Funcionario('marcos', '12222', 2500, 0.05, 2375)
marcos.mostraFuncionario()
marcos.descontar(3000,0.05)
marcos.liquidar(3000,1,1)
marcos.mostraFuncionario()






