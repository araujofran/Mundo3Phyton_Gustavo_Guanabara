
maior = 0
menor = 0
r= 'S'
while r == 'S':
    num = int (input('Digite um valor: '))
    
    if num > maior:
        maior = num
    else:
        menor = num
    r = (input('Quer continuar?[S/N]: ')).strip().upper()

print (f' O maior valor é {maior} e o menor valor é {menor}.')

