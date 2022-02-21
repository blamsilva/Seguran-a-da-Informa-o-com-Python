import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ArquivoaserOcultado.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi Ocultado.")

else:
    print('Arquivo não foi ocultado')