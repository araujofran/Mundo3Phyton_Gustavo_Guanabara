'''
1.Criar um programa que gere cinco número aleatórios
2.Coloca-los em uma tupla 
3.Mostrar a listagem desses numeros 
4.Mostrar o menor e maior valor dessa lista

'''

import random

numAle = (random.randint (0,5,),random.randint (0,5),random.randint (0,5),random.randint (0,5),random.randint (0,5))
print ('Os valores sorteados foram :' , end=' ')
for n in numAle:
    print (f'{n}',end= ' ')
print ('\n')
print (f'O maior valor sorteado foi {max(numAle)}')
print (f'O menor valor sorteado foi {min(numAle)}')
    
   