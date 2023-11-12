'''
1)Crie um programa onde o usuário possa digitar sete valores numéricos 
2)Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
3)No final, mostre os valores pares e ímpares em ordem crescente.'''
listaunica=[]
listapar=[]
listaimpar=[]

for t in range (1,8):
    t=(int(input(f'Digite {t}° valor: ')))
    listaunica.append(t)
for p in listaunica:
    if p % 2 == 0:
        listapar.append(p)
    else:
        listaimpar.append(p)
print (f' A lista Par {sorted(listapar)}')
print (f' A lista Ímpar {sorted(listaimpar)}')

''' Resolução Gustavo Guanabara'''

unica =[[],[]]
valor=0

for c in range(1,8):
    valor= int (input(f'Digite o {c}° valor: '))
    if valor % 2 ==0:
        unica[0].append(valor)
    else:
        unica[1].append(valor)
print (f' A lista unica com duas listas internas par e impar ficou assim\n {unica} \n e a lista Par {sorted(unica[0])} e a lista Ímpar {sorted(unica[1])}')