'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz=[[1,2,3],[4,5,6],[7,8,9]]
soma=0
par=0
listapar=[]
coluna3=[]
soma3=0
segundaLinha=[]
soma2=0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c]=int (input (f'Digite para [{l},{c}]: '))
        soma +=matriz[l][c]
        if matriz[l][c] %2==0:
            par +=matriz[l][c]
            listapar.append(matriz[l][c])
        if matriz[l][c]==matriz[0][2] or matriz[l][c]==matriz[1][2] or matriz[l][c]==matriz[2][2]:
            coluna3.append(matriz[l][c])
            soma3+=matriz[l][c]
        if matriz[l][c]==matriz[1][0] or matriz[l][c]==matriz[1][1] or matriz[l][c]==matriz[1][2]:
            segundaLinha.append(matriz[l][c])
            soma2+=matriz[l][c]


      

for l in range (0,3):
    for c in range (0,3):
        print (f'[{matriz[l][c]:^5}]',end='')
    print()
    
# Soma de todos os valores digitados

print (f' A soma de todos os numeros digitados foram: {soma}. ')

# A soma de todos os numeros pares
print (f' A lista de todos os numeros pares são {listapar}. ')
print (f' A soma dos números pares deu {par}. ')
print('\n')

# Aprendendo a fazer a  captura da terceira coluna

print (f' A  terceira coluna é constituida desse numeros: {coluna3}. Veja compare com a lista completa. ')
for l in range (0,3):
    for c in range (0,3):
        print (f'[{matriz[l][c]:^5}]',end='')
    print()
print (f' A soma dos numeros pertencentes a essa 3ª coluna deu {soma3}. ')

# Analisando a segunda linha e seu maior valor:
print()
print (f' Esses são os valores da segunda linha {segundaLinha}')
print()
print (f' O maior valor dentre os números da segunda linha é o {max(segundaLinha)}. ')
print()
print (f' O resultado da soma dos números da segunda linha foi de : {soma2}. ')
