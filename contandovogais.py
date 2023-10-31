''''
Exercício Python 077: 
1.Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
2.Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla = ('Abacaxi','Caqui', 'Melancia','Amora')

for p in tupla:
    print (f'\n A lista de elementos dessa tupla é : {p.upper()}.Contendo as seguintes vogais : ', end='')
    for vogais in p:
       if vogais.lower() in 'aieou':
           print (f'{vogais}', end='...')