import hashlib

string = str(input('Digite o texto a ser gerado a hash: '))

menu = str(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3)SHA256
                4)SHA513
                Digite o número do hash a ser gerado: '''))
while menu not in "1234":
    print('Opção errada! Escolha novamente.')
    menu = str(input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
                    1) MD5
                    2) SHA1
                    3)SHA256
                    4)SHA513
                    Digite o número do hash a ser gerado: '''))
else:

    if menu == '1':
        resultado = hashlib.md5(string.encode('utf-8'))
        print(f'\nO hash MD5 da string é: {resultado.hexdigest()}')
    elif menu == '2':
        resultado = hashlib.sha1(string.encode('utf-8'))
        print(f'\nO hash SHA1 da string é: {resultado.hexdigest()}')
    elif menu == '3':
        resultado = hashlib.sha256(string.encode('utf-8'))
        print(f'\nO hash da SHA256 string é: {resultado.hexdigest()}')
    elif menu == '4':
        resultado = hashlib.sha512(string.encode('utf-8'))
        print(f'\nO hash SHA512 da string é: {resultado.hexdigest()}')

