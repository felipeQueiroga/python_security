import hashlib

string = input("Digite o texto a ser gerado a assinatura MD5: ")

opcao = input('''Escolha o tipo de criptografia 
    1 = MD5
    2 = SHA1
    3 = SHA256
    4 = SHA512
    0 = Todos a cima
Digite o numero correspondente:''')

if opcao == '1' or opcao == '0':
    resultado = hashlib.md5(string.encode('utf-8')) 
    print('Hash MD5: ', resultado.hexdigest())

if opcao == '2' or opcao == '0':
    resultado = hashlib.sha1(string.encode('utf-8')) 
    print('Hash sha1: ', resultado.hexdigest())

if opcao == '3' or opcao == '0':
    resultado = hashlib.sha256(string.encode('utf-8')) 
    print('Hash sha256: ', resultado.hexdigest())

if opcao == '4' or opcao == '0':
    resultado = hashlib.sha512(string.encode('utf-8')) 
    print('Hash sha512: ', resultado.hexdigest())
else:
    print('A seleção não ocorreu como esperado!')

