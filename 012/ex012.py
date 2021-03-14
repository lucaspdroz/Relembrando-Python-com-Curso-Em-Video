valor_do_produto = float(input('Digite o valor do produto? R$ '))
desconto = int(input('Qual será o desconto? '))

desconto_aplicado = valor_do_produto - ((valor_do_produto * desconto)/100)

print('O  produto que custava R${:.2f}, na promoção de {}% custará: R$ {:.2f}'.format(valor_do_produto,desconto, desconto_aplicado))