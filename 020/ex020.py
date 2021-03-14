from random import shuffle

n1 = str(input('Digite o nome de um aluno:\n'))
n2 = str(input('Digite o nome de outro aluno:\n'))
n3 = str(input('Digite o nome de outro aluno novamente:\n'))
n4 = str(input('Digite o nome de outro aluno novamente:\n'))

lista = [n1,n2,n3,n4]

escolhido = shuffle(lista)

print('O aluno escolhido foi {}'.format((escolhido).title()))