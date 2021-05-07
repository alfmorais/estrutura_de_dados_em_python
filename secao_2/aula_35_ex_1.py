lista = []
contador = 0
while True:
    valor = input('Digite um valor: ')
    lista.append(valor)
    contador += 1
    if contador == 2:
        break

print(lista)

try:
    resultado = int(lista[0]) / int(lista[1])
    print(resultado)
except ValueError:
    pass
except ZeroDivisionError:
    pass
except IndexError:
    pass
except KeyboardInterrupt:
    pass
