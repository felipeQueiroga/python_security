import sys

def contador_letras(lista):
    lista_resultado = []
    for x in lista:
        lista_resultado.append(len(x))
    return lista_resultado       

if __name__ == "__main__":
    lista_teste = ['gato','peixe','tartaruga']
    resultado = contador_letras(lista_teste)
    print(resultado)