lista= [{'nome': 'Fabio', 'sexo': 'M', 'idade': 45.0}, {'nome': 'Paula', 'sexo': 'F', 'idade': 12.0}]
for v in lista:
    for k,v in v.items():
        print (f' {k} = {v} ', end=';')
    print()