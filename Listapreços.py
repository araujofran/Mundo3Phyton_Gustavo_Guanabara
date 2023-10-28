listagem = ('lapis', 1.75,
            'borracha',2,
            'caderno',17.50,
            'caneta',1.88)
print ('-'*40)
print (f'{"LISTAGEM DE PREÇOS":^40}')
print ('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print (f'{listagem[pos]:.<30}', end ='')
    else:
        print (f'R${listagem[pos]:>7.2f}')
print ('-'*40)
    
