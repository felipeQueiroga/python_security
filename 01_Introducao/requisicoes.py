import requests
import sys 

def requisicao_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())

    dados_cep = response.json()
    print(dados_cep['logradouro'])

def requisicao_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    print(response.status_code)
    print(response.json())

    dados_cep = response.json()
    print(dados_cep['name'])
    print(dados_cep['sprites']['front_shiny'])

def retorna_response(url):
    response = requests.get(url)
    print(response.text)
    return response.text    

if __name__ == "__main__":
    requisicao_cep(79077005)
    requisicao_pokemon('pikachu')
    retorna_response('https://globallabs.academy/')