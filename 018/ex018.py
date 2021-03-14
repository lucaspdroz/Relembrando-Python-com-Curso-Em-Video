from math import sin,cos,tan,radians

angle = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angle))
cosseno= cos(radians(angle))
tangente= tan(radians(angle))

print('O âgulo de {}º tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(angle,seno,cosseno,tangente))