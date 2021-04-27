def adicao(n1, n2):
    soma = n1 + n2
    print('A soma dos {:.2f} + {:.2f} = {:.2f}'.format(n1, n2, soma))

def subtracao(n1, n2):
    subtracao = n1 - n2
    print('A subtração dos {:.2f} - {:.2f} = {:.2f}'.format(n1, n2, subtracao))

def divisao(n1, n2):
    try:
        divisao = n1 / n2
        print('A divisão dos {:.2f} / {:.2f} = {:.2f}'.format(n1, n2, divisao))
    except ZeroDivisionError:
        print('n2 = 0, não é possivél fazer a conta')

def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    print('A multiplicação dos {:.2f} * {:.2f} = {:.2f}'.format(n1, n2, multiplicacao))

n1 = int(input('Digite N1: '))
n2 = int(input('Digite N2: '))

adicao(n1, n2)
subtracao(n1, n2)
divisao(n1, n2)
multiplicacao(n1, n2)


