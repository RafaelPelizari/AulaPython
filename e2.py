
print('leia 3 notas e calcule a média./n')
n1 = float(input('n1:'))
n2 = float(input('n2:'))
n3 = float(input('n3:'))
media = (n1 + n2 + n3)/3
print('média:', media)
if(media<=5.0):
    print('reprovado')
elif(media>=7.0):
    print('aprovado')
else:
  print('recuperacao')
