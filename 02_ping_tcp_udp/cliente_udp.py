import socket
import sys

def main():
    try:                 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    except socket.error as e:
        print("Erro ao criar socket: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso!") 
    return s

def envia_msg(sckt, host_alvo, porta_alvo):
    try:
        mensagem = input("Digite a mensagem a ser enviada: ") 
        if mensagem == '':
            fecha_conexao(sckt)

        print("Alvo: {}:{}".format(host_alvo, porta_alvo))
        print("Cliente: " + mensagem)
        sckt.sendto(mensagem.encode() , (host_alvo, int(porta_alvo)))
       
        dados, servidor = sckt.recvfrom(4096)
        dados = dados.decode()
        #Aciona respsota
        print("Cliente: " + dados)

    except socket.error as e:
        print("Erro de conexão UDP: {}".format(e))
        sckt.close()
    except ValueError as ae:
        print("Erro ao converter porta {}: {}".format(porta_alvo, ae))
        sckt.close()

def fecha_conexao(sckt):
    print("Cliente: Fechando a conexão")
    sckt.close()
    sys.exit()

if __name__ == "__main__":    

    sckt = main()

    host = '127.0.0.1'    
    porta = '5432' 
    while 1:
        envia_msg(sckt, host, porta)