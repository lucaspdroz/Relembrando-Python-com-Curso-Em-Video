# conversor de distância

distance = int(input('Uma distância em metros:'))

print('{}km \n{}hm\n {}dam\n  {}m\n {}dm\n {}cm\n {}mm'.format(
    distance /1000,
    distance / 100,
    distance / 10,
    distance,
    distance * 10,
    distance * 100,
    distance * 1000,
))