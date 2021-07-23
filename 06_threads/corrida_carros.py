from threading import Thread
import sys
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:       
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} KM {}'.format(piloto, trajeto))
    print(print('Piloto: ', piloto, ' #Cheguei#'))

if __name__ == "__main__":
   t_carro1 = Thread(target=carro, args=[10, 'luis']) #args
   t_carro2 = Thread(target=carro, args=[20, 'Felipe']) #args

   t_carro1.start()
   t_carro2.start()
