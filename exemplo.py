v = [1, 2, 3, 2, 1, 1, 2, 2, 3, 1]
x = int(input("Entre com um número a ser buscado: "))
pos = []
for i in range(len(v)):
 if v[i] == x:
  pos.append(i)
 print(pos)

