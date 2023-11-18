from datetime import date

ficha={}
lista=[]

ficha['Nome']= str(input('Nome: '))
ano_atual= int (input ('Ano Atual: '))
ano_nascimento= int (input('Ano nascimento: '))
idade = ano_atual - ano_nascimento
ficha['idade']= idade
ficha['ctps']= int (input('Carteira de Trabalho(0 não tem): '))
if ficha['ctps']>0:
    ficha['contratação']= int(input('Ano de contratação: '))
    ficha['salário']= int(input('Salário: R$ '))
    ficha['aposentadoria']= ((ficha['contratação']+35)-ano_atual)+idade
lista.append (ficha.copy())
print (40*'-=')
for k,v in ficha.items():
    print (f'{k} tem o valor  {v}')
print ()
print (40*'-=')  


