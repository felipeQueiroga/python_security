import socket

try:                 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket criado com sucesso!")
except socket.error as e:
    print("Erro ao criar socket: {}".format(e))
    sys.exit()

host = '127.0.0.1'    
porta = 5432  
log = []

s.bind((host, 5432))  #ligacao
mensagem = "\nServidor: Ola, recebi sua mensagem"

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print("Servidor: Respondendo mensagem...")
        s.sendto(dados + (mensagem.encode()) , end)
        log.append(dados) 
        print(log)
main()