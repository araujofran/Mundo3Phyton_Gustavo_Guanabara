'''Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso,mostre:                                                                                                                                               
 A) Quantos números foram digitados.                                                                                                                    
 B) A lista de valores, ordenada de forma decrescente.                                                                                          
 C) Se o valor 5 foi digitado e está ou não na lista.'''
lista=[]
resposta = 'S'
while resposta == 'S':
    lista.append(int(input('Digite um valor: ')))
    resposta = str (input('Quer continuar?[S/N]: ... ')).upper() .strip()
    if resposta=='N':
        break
print(30*'-+.')
print (f'Os numeros digitados foram: {lista} e quantidade de numeros digitados foram {len(lista)} numeros.')
print(30*'-+.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}. ')
if 5 in lista:
    print (f'Na lista {lista} veja que o numero 5 está presente...')
else:
    print ('O numero 5 NÃO está presente na lista SEU otário!')