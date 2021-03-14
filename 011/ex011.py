altura = float(input('Digite a da sua altura parede em metros'))
largura = float(input('Digite a da sua largura parede em metros'))

area = altura * largura
tinta = area / 2

print('sua parede tem a dimenção de {} por {} e sua área é de {}m².\nE você precisará de {}L de tinta'.format(altura,largura,area,tinta)) 


