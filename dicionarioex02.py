import random,time

jogadado={}
jogadado['jogador1']= random.randint(0,6)
jogadado['jogador2']= random.randint(0,6)
jogadado['jogador3']= random.randint(0,6)
jogadado['jogador4']= random.randint(0,6)



print('===============Valores sorteados=================')
for k,v in jogadado.items():
    print(f'O {k} tirou o nº {v}. ')
    time.sleep(1.15)
  
print('===============Ranking dos Jogadores=============')    
print()
count= 1
for i in sorted (jogadado,key=jogadado.get,reverse=True):
    print(f'{count}º lugar: ', end='') 
    print (i,'com ',jogadado[i])
    time.sleep(1.15)
    count+=1
    
print('\n')
    