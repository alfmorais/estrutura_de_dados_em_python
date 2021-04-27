numero = int(input('Escolha um numero: '))

contador = 0
while True:
    total = numero * contador
    print('{} x {} = {}'.format(numero, contador, total))
    contador += 1
    if contador == 11:
        break
