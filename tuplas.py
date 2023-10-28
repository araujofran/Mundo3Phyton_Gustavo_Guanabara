legumes = ('A','B','C','D','E')

print (len(legumes))

for pos, comida in enumerate(legumes):
    print (f'Eu vou selecionar {comida} na posição {pos}')

print ('\n')
print(f'A letra C está em qual posição? Esta na posição: {legumes.index('C')}')
print ('\n')
print(f'A letra C aparece : {legumes.count('C')} veze(s)')

print ('\n')