#crie dois vetores com nome e notas de 4 alunos 
#mostre o nome e a nota dos alunos acima da media da turma 
from socket import SOMAXCONN
nomes = ['ana','pedro','lucas','carlos']
notas =[10,9,6,7]



#media da turma 
soma = 0
for nota in notas:
    soma +=nota
media = soma/len(notas)
print('media da turma:', media)
for i in range(len(notas)):
    if notas[i]> media:
        print('aluno com nota acima da media:', nomes[i],'nota: ', notas[i])