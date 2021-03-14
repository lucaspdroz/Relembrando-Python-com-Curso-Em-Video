celcius = float(input('Informe a temperatura em ºC:\n'))
fahrenheit = celcius * 1.8 + 32
kelvin =  (fahrenheit + 459.67) / 1.8 
Réaumur = (fahrenheit - 32) / 2.25

print('------------------------------------')
print('{:.2f}ºC\n{:.2f}ºF\n{:.3f}K\n{:.3f}ºRa (Réaumur)'.format(celcius,fahrenheit,kelvin,Réaumur))