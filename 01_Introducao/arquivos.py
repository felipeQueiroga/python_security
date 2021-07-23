import sys
import shutil

def criar_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'w')
    arquivo.close

def atualiza_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close

def ler_arquivo(arquivo):
    arquivo = open(arquivo, 'r')
    conteudo = arquivo.read()
    return conteudo

def calcula_media(arquivo):
    arquivo = open(arquivo, 'r')
    aluno_nota = arquivo.read()

    lista_resultado = []
    linhas = aluno_nota.split('\n')
    for x in linhas:
        colunas = x.split(',')
        aluno = colunas[0]
        colunas.pop(0)
        calc_media = lambda notas: sum([int(i) for i in notas]) / 4
        media = calc_media(colunas)
        lista_resultado.append({aluno:media}) #dicionario
    return lista_resultado
    arquivo.close

def copia_arquivo(path):
    shutil.copy(path, 'copia.txt')

def move_arquivo(path):
    shutil.move(path, 'arquivo_movido.txt')

if __name__ == "__main__":
    path = '01_Introducao/notas.txt'
    
    criar_arquivo(path)
    ler_arquivo(path)

    aluno = 'Rafael,10,5,5,8\n'
    aluno2 = 'Anna,7,8,2,8\n'
    aluno3 = 'Lucas,5,8,7,8\n'

    atualiza_arquivo(path, aluno)
    atualiza_arquivo(path, aluno2)
    atualiza_arquivo(path, aluno3)

    lista_medias = ler_arquivo(path) 
    print(lista_medias)

    print(calcula_media(path))

