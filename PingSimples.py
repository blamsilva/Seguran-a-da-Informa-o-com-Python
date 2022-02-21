import os #Importa o Módulo ou Biblioteca OS (Integra os programas e recursos do S.O)

print('#'*60)

ip_ou_host = input('Digite o Ip ou host a ser verificado: ') # Criando uma variável que recebe o IP
print('-'*60)
os.system(f'ping -n 6 {ip_ou_host}') #Chamando o system da biblioteca OS - chamando o comando ping com seis disparos.
# print('-'*60)
