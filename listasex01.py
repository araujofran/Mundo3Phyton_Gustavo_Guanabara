'''Faça um programa que:
a)Leia 5 valores numéricos 
b)Guarde-os em uma lista. 
c)No final, mostre qual foi o maior e o menor valor digitado 
d)Mostre as suas respectivas posições na lista.'''

valores= []

for cont in range (0,5):
   valores.append(int (input('Digite um valor: ')))
   
print (15* '-=')
for p,v in enumerate(valores):
   print (f'Na posição {p} tenho o valor {v}...')
   
print('\n')
print (15* '-=')   
print (f'A lista digitada foi {valores}. ')
print (15* '-=')
print (f'O maior valor dessa lista é : {max(valores)}.As posições do maior valor são: ',end='')
for i, maior in enumerate (valores):
   if maior == max(valores):
      print (f'{i}. ',end='...')
print ()
print (f'O menor valor dessa lista é : {min(valores)}.As posições do menor valor são: ',end='')
for i, menor in enumerate (valores):
   if menor == min(valores):
      print (f'{i}. ',end='...')
print ()
print ('FIM!!!')
    


 
