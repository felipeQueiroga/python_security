from Ping.ping_simples import ping

arquivo = open('02_ping_tcp_udp/ips.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
Lista_ping = conteudo.split('\n')

for x in Lista_ping:
    ping(x)


