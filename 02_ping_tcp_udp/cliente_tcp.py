import socket
import sys 

def main():
    try:                 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Erro ao criar socket: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!")

    host_alvo = input("Digite o host a ser conectado: ")
    porta_alvo = input("Digite a porta a ser conectado: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com sucesso: {}:{}".format(host_alvo, porta_alvo))
        #s.send(b'Envia mesagem')
        s.shutdown(5)
    except socket.error as e:
        print("Erro de conexão TCP: {}".format(e))
        sys.exit()
    except ValueError as ae:
        print("Erro ao converter porta {}: {}".format(porta_alvo, ae))
        sys.exit()


if __name__ == "__main__":  
    main()
