def calculo_fahrenheit():
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (9 * celsius + 160) / 5
    print('A temperatura  {:.2f}° Celsius corresponde a {:.2f}° Fahrenheit'.format(celsius, fahrenheit))

calculo_fahrenheit()
