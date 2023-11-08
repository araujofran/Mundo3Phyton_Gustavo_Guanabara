'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

nalista=[]

for cont in range (0,5):
    digitado=(int(input('Digite um número: ... ')))
    if cont == 0 or digitado >nalista[-1]:
        nalista.append(digitado)
        print ('Adicionado na posição final da lista!')
    else:
        pos=0
        while pos<len(nalista):
            if digitado<=nalista[pos]:
                nalista.insert(pos,digitado)
                print (f'Adicionado na posição {pos} da lista! ')
                break
            pos+=1
  
print (30*'-=')
print (nalista)
