#impostacoes
from funcao_class import Calculadora 
from contador_letras import contador_letras

mult = Calculadora.soma(1 , 25)
print(mult) 

lista = ['5', 'luis felipe querioga de araujo']
print(contador_letras(lista))

#exemplo lambda 
contador_letras_lambda = lambda lista: [len(x) for x in lista]
print(contador_letras_lambda(['1234']))

soma = lambda a, b: a + b
