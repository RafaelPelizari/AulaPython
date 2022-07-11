from msilib.schema import Class
from socket import CAN_RAW_RECV_OWN_MSGS


class Carro: 
    def __init__(self, consumo): 
        self.consumo = consumo
        self.nivelCombustivel = 0 

    def andar(self, distancia):
        temp = distancia/self.consumo
        self.nivelCombustivel -= temp 

    def obterGasolina(self): 
        return self.nivelCombustivel

    def adicionarGasolina(self, qtd): 
        self.nivelCombustivel += qtd 

meuFusca = Carro(8)
meuFusca.AdicionarGasolina(50) 
meuFusca.andar(300)  
print(vars(meuFusca)) 
print (meuFusca.obterGasolina)
