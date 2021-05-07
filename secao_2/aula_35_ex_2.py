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
    print('Um dos valores que foi digitado é do formato "caracter".')
except ZeroDivisionError:
    print('Um dos valores que foi digitado é ZERO.')
except IndexError:
    print('Conta não pode ser executado porque a lista não tem esse index')
except KeyboardInterrupt:
    print('Execução interrompida pelo usuario com sucesso')
    
