'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

# (1*2)+5
''' estudar mais e encontrar uma outra tecnica para resolver esse exercicio'''
f=[]
f = str(input('Digite a formúla matematica: '))
cont =1
while p in range (0,len(f)-1):
    if ( f [p] == f [p+1] ):
     cont +=1
print (f' O numero total de parenteses é : {cont}')

