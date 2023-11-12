'''
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
[P[0,0]][P[0,1]][P[0,2]]
[P[0,0]][P[0,0]][P[0,0]]
[P[0,0]][P[0,0]][P[0,0]]

'''

print (25*'-=')
print('--------------------MATRIZ 3X3--------------------')
print (25*'-=')

l1 = [[],[],[]]
l2 = [[],[],[]]
l3 = [[],[],[]]
valor = 0
cont=0

for p in range (0,3):
    if cont==0:
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l1[0].append(valor)
        cont +=1
    if cont==1: 
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l1[1].append(valor)
        cont +=1
    else:
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l1[2].append(valor)
        cont +=1
    if cont >=3:
        break
for p in range (0,3):
    if cont==0:
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l2[0].append(valor)
        cont +=1
    if cont==1: 
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l2[1].append(valor)
        cont +=1
    else:
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l3[2].append(valor)
        cont +=1
    if cont >=3:
        break
print(l1)
print(l2)