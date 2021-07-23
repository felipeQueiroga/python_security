import hashlib

arquivo1 = '04_gerar_senhas/a.txt'
arquivo2 = '04_gerar_senhas/b.txt'


hash1 = hashlib.new('ripemd160') #sha1, sha256, md5 
hash1.update(open(arquivo1, 'rb').read())  #'rb'=leitura binaria

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() == hash2.digest():
    print('O arquivo: {} é igual ao arquivo: {}'.format(arquivo1, arquivo2))
else: 
    print("arquivos diferente")