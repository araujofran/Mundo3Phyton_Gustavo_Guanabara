'''
1)Crie um programa que leia nome e duas notas de vários alunos
2)Guarde tudo em uma lista composta. 
3)No final, mostre um boletim contendo a média de cada um 
4)e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

r='S'
ficha=list()

while r ==  'S':
    
    nome=str(input('Nome:'))
    n1=int (input('Nota 1: '))
    n2=int (input('Nota 2: '))
    media= (n1+n2)/2

    ficha.append([nome,[n1,n2],media])
    r= str(input(f'Quer continuar?[S/N] ')).upper()
    if r=='N':
        break

print (30*'==')
print (f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print (26*'-')

for i,a in enumerate(ficha):
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
while True:
    print (35*'-')
    opc=int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc==999:
        print('Fim!')
        break
    if opc <= len(ficha)-1:
        print(f'As notas do aluno {ficha[opc][0]} são {ficha[opc][1]}')
