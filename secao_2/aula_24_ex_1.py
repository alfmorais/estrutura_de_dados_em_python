lista_numeros = []

contador = 0
while True:
    num = float(input('Digite um numero: '))
    lista_numeros.append(num)
    contador += 1
    if contador == 5:
        break

soma = 0

for numero in lista_numeros:
    soma = soma + numero

print(soma)
    
