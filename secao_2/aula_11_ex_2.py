tempo = float(input('Digite o tempo da viagem: '))
vdmed = float(input('Digite a velocidade média da viagem: '))

def distancia(tempo, vdmed):
    distancia = tempo * vdmed
    distancia = round(distancia, 2)
    return distancia

def litros_usados(distancia, autonomia=12):
    litros = distancia / autonomia
    litros = round(litros, 2)
    return litros

distancia = distancia(tempo, vdmed)
litros = litros_usados(distancia)

print('A viagem teve a distância total percorrida {} e a quantidade de combustivel utilizada foi {} litros'.format(distancia, litros))
