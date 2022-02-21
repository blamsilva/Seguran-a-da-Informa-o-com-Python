import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)
print(endereco)

iprede = "192.168.0.100/24"
rede = ipaddress.ip_network(iprede, strict=False)
print(rede)

for ip in rede:
    print(ip)