salario = float(input('Qual é o slaário do funcionário? R$ '))
adicional_salario = int(input('Qual será o adicional_salario? '))

adicional_salario_aplicado = salario + ((salario * adicional_salario)/100)

print('Um funcionário que ganhava R${:.2f}, com {}% de aumento receberá: R$ {:.2f}'.format(salario,adicional_salario, adicional_salario_aplicado))