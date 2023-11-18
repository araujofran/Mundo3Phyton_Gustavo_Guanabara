
#lista.append (ficha.copy())
dicionario={}
lista=[]
npessoas=0
soma=0

mulher=[]
acima={}
acimaMedia=[]
r='S'
while r=='S':
    n=str(input('Nome: '))
    dicionario['nome']=n
    s=str(input('Sexo [M/F]? ')).upper()
    dicionario['sexo']=s
    if s=='F':
        mulher.append(n)
    id=float(input('Idade: '))
    dicionario['idade']=id
    npessoas+=1
    soma+=id
    lista.append(dicionario.copy())
    r=str(input('Continua?[S/N] ')).upper()
    if r=='N':
        break
media=soma/npessoas
print()
print(40*'=-')
print(f'A) Ao todo temos {npessoas} pessoas cadastradas.')
print(f'A) A média de idade é de {media:.2f} anos. ')
print(f'C) As mulheres cadastradas foram {mulher}')
print(f'D) Lista das pessoas que estão acima da média: ')
for v in lista:
    if v['idade']>media:
        for k,v in v.items():
            print (f' {k} = {v} ', end=';')
    print()
print(40*'=-')
print('\n')