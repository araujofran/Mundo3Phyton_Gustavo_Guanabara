'''DESAFIO 02 *MUNDO 03 PHYTON*

a) Escrever os primeiros colocados no brasileirão na ordem de colocação
b) Exibir apenas os 5 primeiros
c) Exibir depois a zona de rebaixamento
d) Mostra sorted (ordem alfabética)
c) Exibir em que posição está o Corinthians

'''

colocação = ('Corinthians','Palmeiras','São Paulo','Botafogo','Santos','Flamengo','Inter','Vasco')
print('\n')

print(f' No total foram {len(colocação)} colocados! \n' )
print (f'Os cinco primeiros colocados foram: {colocação[:5]} \n')
print(f'Os que ficaram na zona de rebaixamento foram {colocação[5:]} \n')
print(f' A ordem alfabetica dos times {sorted(colocação)}\n')

print (f'O Corinthians meu timão ocupa a posição {colocação.index('Corinthians')}')
