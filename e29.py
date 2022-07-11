class Robo: 
    def __init__ (self, nome, fome, saude, idade): 
        self.nome = str(nome) 
        self.fome = str(fome) 
        self.saude = str(saude) 
        self.idade = str(idade) 
    def getNome(self):  
        return self.nome 
    def setNome(self,nome): 
        self.nome = nome 
    def getSaude(self): 
        return self.saude 
    def setIdade(self,idade): 
        self.idade = idade 
    def alterar(self): 
        self.getSaude() 
robo = Robo('Einsten','muita','boa',4 )
print (robo.alterar()) 
print (vars(robo)) 
