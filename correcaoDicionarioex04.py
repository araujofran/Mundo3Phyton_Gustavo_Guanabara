'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

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
