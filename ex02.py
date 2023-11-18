'''JOGO DA MEGASENA
1)Faça um programa que ajude um jogador da MEGA SENA 
2)a criar palpites.
3)O programa vai perguntar quantos jogos serão gerados 
4)e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

'''
import random,time


jogos=0


lista=[]


print (30*'=')
print ('---------JOGOMEGASENA---------')
print (30*'=')

print (' Vamos Jogar! ')
print()
jogos= int (input('Quantos jogos serão sorteados? '))

for j in range (1,jogos+1):
    
    sorteio  = random.sample (range(60),k=6)
    print (f' No {j}º   jogo foram os numeros {sorteio}')
    time.sleep(1)
print ()

sorteio.clear()   
print()




