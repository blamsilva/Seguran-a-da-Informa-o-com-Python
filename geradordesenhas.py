import random, string

tamanho = int(input("Digite o tamanho da senha que você quer gerar: "))
chars = string.ascii_letters + string.digits + '!@#$%&8()-=+çÇ'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))



