idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Idade informada está invalida')

elif idade >= 0 and idade <= 12:
    print('Você está classificado como criança')

elif idade >= 13 and idade <= 17:
    print('Você está classificado como adolescente')

elif idade >= 18:
    print('Você está classificado como adulto')
