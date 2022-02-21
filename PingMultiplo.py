import os # Importa a biblioteca OS
import time # Importa a Biblioteca time

with open('hosts.txt') as file: #abre o arquivo de ips
    dump = file.read() #le o arquivo de ips
    dump = dump.splitlines() # le os ips por linha

    for ip in dump:
        print(f'Verificando o Ip: {ip}')
        print('-'*60)
        os.system(f'ping -n 2 {ip}')
        print('-' * 60)
        time.sleep(5)