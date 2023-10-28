

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while True:
   
   digite = int (input('Digite um número de 0 a 5 : '))
   
   if 0<= digite <=5:
        break
   
   print('Digite novamente.', end=' ')
    
print (f'O numero digitado foi {digite} e a frase por extenso é {extenso[digite]}!')  



