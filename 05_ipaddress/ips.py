import ipaddress

ip_str = '127.0.0.0'
ip_net_str = '10.0.0.1/24' #24 = 24 bits aplicados para o prefixo de rede
                           #e os restantes 8 bits reservados para endereçamento

endereco = ipaddress.ip_address(ip_str)
print(endereco)

endereco_net = ipaddress.ip_network(ip_net_str, strict=False)
print(endereco_net)

print('Lista de IP:')
for ip in  endereco_net:
    print(ip)

#Classes    Faixas IP	                    Número de IPs
#Classe A	10.0.0.0    – 10.255.255.255	16.777.216
#Classe B	172.16.0.0  – 172.31.255.255	1.048.576
#Classe C	192.168.0.0 – 192.168.255.255	65.535

#Endereço de classe A
#Notação CIDR   Máscara           Nº IPs
#/8             255.0.0.0         16.777.216    (começa com 8 bits 1)

#Endereços de classe B
#Notação CIDR   Máscara           Nº IPs
#/16            255.255.0.0       65.536        (começa com 16 bits 1)
#/17            255.255.128.0     32.768        (começa com 17 bits 1)
#/18            255.255.192.0     16.384        (começa com 18 bits 1)
#/19            255.255.224.0     8.192         (começa com 19 bits 1)
#/20            255.255.240.0     4096          (começa com 20 bits 1)
#/21            255.255.248.0     2048          (começa com 21 bits 1)
#/22            255.255.252.0     1024          (começa com 22 bits 1)
##/23            255.255.254.0     512           (começa com 23 bits 1)

#Endereços de classe C
#Notação CIDR   Máscara           Nº IPs
#/24            255.255.255.0     256           (e assim por diante...)
#/25            255.255.255.128   128
#/26            255.255.255.192   64
##/27            255.255.255.224   32
#/28            255.255.255.240   16
#/29            255.255.255.248   8
#/30            255.255.255.252   4
#/31            255.255.255.254   2
#/32            255.255.255.255   1