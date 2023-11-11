'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final mostre:                                                                  
A) Quantas pessoas foram cadastradas.                                                             
B) Uma listagem com as pessoas mais pesadas.                                                                 
C) Uma listagem com as pessoas mais leves.'''

dados=[]
listageral=[]
r ='S'
maior=0
menor=0
while r=='S':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(listageral)==0:
        maior=menor=dados[1]
    else:
        if dados[1]> maior:
            maior=dados[1]
        elif dados[1]< menor:
            menor=dados[1]
    listageral.append(dados[:])
    dados.clear()
    r = (input('Quer continuar?[S/N] ')).upper().strip()

print(f'A lista geral de pessoas ficou assim: {listageral} \n e o total de pessoas cadastradas foi de : {len(listageral)}! ')
for p in listageral:
    if p[1] ==maior:
        print (f'Nome {p[0]} é o maior peso com {p[1]} kg.')
for p in listageral:
    if p[1] == menor:
        print (f'Nome {p[0]} é o menor peso com {p[1]} kg.')


