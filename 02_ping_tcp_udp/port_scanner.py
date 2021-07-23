import socket
import sys 

def main():
    host_alvo = input("Digite o host a ser conectado: ")
    porta_padrao = 80

    for x in range(9999):
        try:                 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            s.settimeout(0.2)
      
            codigo = s.connect_ex((host_alvo, int(x)))
            if codigo == 0:
                print("{}:{}".format(host_alvo, x))
                s.shutdown(0)              
        except socket.error as e:
            print("Erro TCP: {}".format(e))
            sys.exit()

if __name__ == "__main__":  
    main()
