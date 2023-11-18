
dados={}
dados['nome']=str(input('Nome do jogador: '))
partidas= int (input('Quantas partidas ele jogou? '))
dados['partidas']=partidas
c=0
gols=[]
dados['gols']= gols
nºpartida=[]


somagols=0

while c <=dados['partidas']-1:
    g= int (input(f'Quantos gols na partida {c}? '))
    gols.append(g)
    nºpartida.append(c)
    somagols+=g
    c+=1
dados['total']=somagols
gols_dicionario=dict(zip(nºpartida,gols)) 
print ()
print(20*'==')
print('AQUI A PROVA DOS NOVE')
print(20*'==')
print(f'A lista do numero da posição do numero de partidas: {nºpartida}.' )
print(20*'==')
print(f'Aqui a lista do numero de gols/partida {gols}.')
print(20*'==')
print(f'Aqui transformei as listas em dicionario com sua posição/partida {gols_dicionario} .')
print(20*'==')
print()

del dados['partidas']
print()
print(35*'==')
print(dados)
print(35*'==')
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}. ')
print()
print(35*'==')
print (f'O jogador {dados["nome"]} jogou {partidas} partidas e fez {somagols} gols. ')
print()

for k,v in gols_dicionario.items():
    print (f'=> Na partida [0{k}] foram {v} gols...')

print()

    
    