def variaveis():
    velocidade = float(input("Digite a velocidade: "))
    tempo = float(input("Digite o tempo: "))
    return velocidade, tempo

def distancia(tempo, velocidade):
    distancia = tempo * velocidade
    distancia = round(distancia, 2)
    return distancia

def quantidade_litros(distancia):
    autonomia = 12
    litros_usado = distancia / 12
    litros_usado = round(litros_usado, 2)
    return litros_usado

def resultado(velocidade, tempo, distancia, litros_usado):
    return f'Viajando em uma velocidade média de {velocidade} km/h, em um tempo de {tempo} h, a quantidade de gasolina foi {litros_usado} e a distância foi de {distancia} km'

velocidade, tempo = variaveis()
distancia = distancia(tempo, velocidade)
litros_usado = quantidade_litros(distancia)
resultado = resultado(velocidade, tempo, distancia, litros_usado)
print(resultado)
