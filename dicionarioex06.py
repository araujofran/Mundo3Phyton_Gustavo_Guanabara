'''
'''
dicionario={}
lista=[]
gols=[]
totalgols=0
r='S'
count=0
partidas=0
print(40*'-=')
while r=='S':
    dicionario['nome']=str(input('Nome do Jogador: '))
    p=int(input(f'Quantas partidas {dicionario["nome"]} jogou? ' ))
    while partidas<p:
        g=int(input(f'Quantos gols na partida {count}? '))
        count+=1
        partidas+=1
        gols.append(g)
        totalgols+=g
     
    dicionario['gols']=gols[:]
    dicionario['Total']=totalgols
    lista.append(dicionario.copy())
    r=str(input('Quer continuar? [S/N] ')).strip().upper()
    partidas=0
    count = 0
    totalgols=0
    del gols[:]
    while r not in 'SsNn':
        r=str(input('Resposta Incorreta!\n Quer continuar? [S/N] ')).strip().upper()
    if r=='N':
        break

print(40*'-=')
m=0
while m <1:
    for k in lista:
        for k in k.keys():
            print (f'{k}',end=' ')
    m+=1
print()
print(40*'-=')
for v in lista:
    for v in v.values():
        print (f'{v} ', end=' ')
    print()
