
digite = 0
count=0
digite = int (input('Digite um número de 0 a 5 : '))
while digite <=5:
    if count > 10:
        break
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

print (15*'-=')

print (f'O numeral  digitado foi {digite} e a expressão por extenso é {extenso[digite]}!')

print('\n')
count +=1
while digite >5:
    denovo= input ('Tente Novamente!!! Digite um numero entre 0 e 5 :')
count=0
while denovo <=5 :
    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

    print (15*'-=')

    print (f'O numeral  digitado foi {denovo} e a expressão por extenso é {extenso[denovo]}!')
       
    print('\n')
    count +=1
    if count > 10:
        break

    print('Obrigado')