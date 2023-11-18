from datetime import datetime

ficha={}
lista=[]

ficha['Nome']= str(input('Nome: '))
ano_nascimento= int (input('Ano nascimento: '))
idade = datetime.now().year - ano_nascimento
ficha['idade']= idade
ficha['ctps']= int (input('Carteira de Trabalho(0 não tem): '))
if ficha['ctps']>0:
    ficha['contratação']= int(input('Ano de contratação: '))
    ficha['salário']= int(input('Salário: R$ '))
    ficha['aposentadoria']= ((ficha['contratação']+35)-datetime.now().year)+idade
lista.append (ficha.copy())
print (40*'-=')
for k,v in ficha.items():
    print (f'{k} tem o valor  {v}')
print ()
print (40*'-=')  


