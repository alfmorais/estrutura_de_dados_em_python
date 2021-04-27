nota_1 = float(input('Digite nota 1: '))
nota_2 = float(input('Digite nota 2: '))
nota_3 = float(input('Digite nota 3: '))
nota_4 = float(input('Digite nota 4: '))
nota_5 = float(input('Digite nota 5: '))

notas = [nota_1,
         nota_2,
         nota_3,
         nota_4,
         nota_5]

def media(somatoria):
    media = somatoria / 5
    media = round(media, 2)
    return media

somatoria = 0

for nota in notas:
    somatoria += nota

media = media(somatoria)
print(media)
