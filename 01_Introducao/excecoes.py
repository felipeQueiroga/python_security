lista = [1, 10]

try:
    x = a
    divisao = 10 / 0
    numero = lista[30]
except ZeroDivisionError:
    print('Não foi possivel realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar indice')
except BaseException as ex:
    print('Um erro foi gerado: {}'.format(ex)) 
finally:
    print('Fiz isso por final')
