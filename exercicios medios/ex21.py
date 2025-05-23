'''
Solicite ao usuario 10 numeros, armazene em uma lista e remova todos os numeros
pares usando remove.

'''

numeros = []

for i in range(10):
    num = int(input('Digite um número: '))
    numeros.append(num)
    
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)
        
print(numeros)
