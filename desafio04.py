'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

count =1
lista =(0,)

while count <= 5:
    n = int(input('Digite um numero: '))
    count +=1
    lista =(n)
print (lista)