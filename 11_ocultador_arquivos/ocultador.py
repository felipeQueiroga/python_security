import ctypes 

atributos_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('11_ocultador_arquivos/arquivo_oculto.txt' , atributos_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Houve um problema. O arquivo não foi ocultado!")