
count=0
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')


for count in extenso:

   digite = int (input('Digite um número de 0 a 5 : '))
   print (f'O numeral  digitado foi {digite} e a expressão por extenso é {extenso[digite]}!')
for count in not extenso:
    
    digite = int (input('Digite novamente um número de 0 a 5 : '))
    
    print (f'O numeral  digitado foi {digite} e a expressão por extenso é {extenso[digite]}!')

else:
    print (f'O numeral  digitado foi {digite} e a expressão por extenso é {extenso[digite]}!')


