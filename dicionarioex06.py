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
        g=int(input(f'Quantos gols na partida {count+1}? '))
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
print('cod ',end='')
for i in dicionario.keys():
    print(f'{i:<15} ',end='')
print()
print(40*'-=')

for k,v in enumerate(lista):
    print(f' {k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(40*'-=')
while True:
    busca = int (input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}: ')
        for i, g in enumerate(lista[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
        print(40*'-=')
print('<< VOLTE SEMPRE >>')