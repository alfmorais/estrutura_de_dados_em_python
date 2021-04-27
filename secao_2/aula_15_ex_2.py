def media(m1, m2, m3):
    media = (m1 + m2 + m3)/3
    media = round(media, 1)
    return media

m1 = float(input('Digite a M1: '))
m2 = float(input('Digite a M2: '))
m3 = float(input('Digite a M3: '))

media = media(m1, m2, m3)
print(media)

if media >= 0.0 and media <= 4.0:
    print('Reprovado')

elif media >= 4.1 and media <= 6.0:
    print('Exame')

elif media > 6.0:
    print('Aprovado')
