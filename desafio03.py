'''
1.Criar um programa que gere cinco número aleatórios
2.Coloca-los em uma tupla 
3.Mostrar a listagem desses numeros 
4.Mostrar o menor e maior valor dessa lista

'''

import random

c=0

maior =0
menor = 0
tupla = 0,
while c < 5:
   
    numAle = random.randint (0,5)
    print (numAle, end=' ')
    c+=1
    tupla = tupla + (numAle)
print ('\n')
print (8*'h')
print (tupla)