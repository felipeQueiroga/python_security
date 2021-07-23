import itertools 
import string

#chars = string.digits

chars = input("Entre com a string a ser permutada: ex(luis123@) \n")

resultado = itertools.permutations(chars, len(chars))

for i in resultado:
    print(''.join(i))
    if 'sanethay@' == ''.join(i):
        break
    if 'teste123' == ''.join(i):
        break