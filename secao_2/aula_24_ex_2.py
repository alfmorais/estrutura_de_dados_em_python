notas = {
    "Alfredo": [5.0, 9.5, 8.7, 7.5],
    "Joaquim": [9.9, 7.5, 6.8, 7.9],
    "Helena": [6.5, 7.9, 8.8, 9.5]
    }

def soma_media(lista):
    media = sum(lista) / 4
    return media

for k in notas:
    nota = notas.get(k)
    media = soma_media(nota)
    media = round(media, 2)
    print(k + ' ficou com a média ' + str(media))
