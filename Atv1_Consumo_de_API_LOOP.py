import requests

url = 'https://viacep.com.br/ws/'
cep_inicial = 30140071
formato = '/json/'

for i in range(5):
    cep = str(cep_inicial + i)
    r = requests.get(url + cep + formato)

    if r.status_code == 200:
        print(f"\n=== Resultado do CEP {cep} ===")
        dados = r.json()
        print(dados)
        print()
    else:
        print(f"Nao houve sucesso na requisicao para o CEP {cep}.")
