

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while True:
     
     digite = int (input('Digite um número de 0 a 5 : '))
     if 0<= digite <=5:
          break
         
     print('Digite novamente.', end=' ')
print (f'O numero digitado foi {digite} e a frase por extenso é {extenso[digite]}!')
resp = str (input('Você quer continuar? [S/N] ')).strip().upper() 

while resp  in 'S':
     while True:
     
          digite = int (input('Digite um número de 0 a 5 : '))
          if 0<= digite <=5:
               break
         
          print('Digite novamente.', end=' ')
     print (f'O numero digitado foi {digite} e a frase por extenso é {extenso[digite]}!')
     resp = str (input('Você quer continuar? [S/N] ')).strip().upper()
     if resp == 'N':
          break

print (f'O numero digitado foi {digite} e a frase por extenso é {extenso[digite]}!')
print ('OBRIGADO!')


