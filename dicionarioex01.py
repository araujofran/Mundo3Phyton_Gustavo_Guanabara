'''
1. Nome dos alunos
2. Mostre a média
3. Situação aprovado ou reprovado
'''
r= 'S'
alunos= {}
ficha=[]
while r == 'S':
    alunos ['nome']= str(input ('Nome do Aluno: '))
    alunos ['nota1']= float(input('Digite a Nota 1: '))
    alunos ['nota2']= float (input('Digite a Nota 2: '))
    alunos['media']= (float(alunos['nota1']+alunos['nota2'])/2)
    if alunos['media']>=7:
        alunos['status']= 'APROVADO!'
    else:
        alunos['status']= 'REPROVADO'
    ficha.append(alunos.copy())
    
    r = str(input('Quer continuar?[S/N] ')).strip().upper()
    if r == 'N':
        break
print (87*'=')
print ('--------------------------------BOLETIM------------------------------------------------')
print (87*'=')
           
for i in ficha:
    for k, v in i.items():
        print (f'{k:<4}: {v:^8}',end=' ')
    print()
print (87*'=')
print ('\n')
        
