'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

print (82*'=')
print (19*'=',end='' )
print ('APRENDENDO COM EXERCÍCIOS DE LISTA EM PYTHON',end='' )
print (19*'=')
print (82*'=')
print('\n ')

lista=[]
pares=[]
impares=[]
while True:
    n=(int(input('Digite um valor: ')))
    lista.append(n)
    if n %2 ==0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()
    if resp in'N':
        break


print (f' Os números dessa lista {lista}. \n Os números pares são {pares}. \n E os números ímpares são {impares}.')