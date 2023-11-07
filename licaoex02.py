'''
a)Crie um programa onde o usuário possa digitar vários valores numéricos b)Cadastre-os em uma lista
c)Caso o número já exista lá dentro, ele não será adicionado. 
d)No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores=[]
resposta = 'S'

while resposta =='S':

    v=(int(input('Digite um valor: ')))

    if v not in valores:
        valores.append(v)
        print ('Adicionado na lista...')
    elif v in valores:
        print ('Valor duplicado! Não será contabilizado!')
     
    resposta = (input('Quer Continuar?[S/N]')).upper().strip()
    
    if resposta == 'N':
        break
   
print (valores)  
valores.sort()
print(valores)

