import requests

url = 'https://viacep.com.br/ws/'
uf = 'MG'
cidade = 'Belo Horizonte'
logradouro = 'Rua dos Aimores'
formato = '/json/'

consulta_url = f"{url}{uf}/{cidade}/{logradouro}{formato}"

r = requests.get(consulta_url)

if r.status_code == 200:
    resultados = r.json()
    
    if isinstance(resultados, list) and resultados:
        print(f"\n=== Resultados para {logradouro}, {cidade} - {uf} ===\n")
        for item in resultados:
            print(f"CEP: {item.get('cep')}")
            print(f"Logradouro: {item.get('logradouro')}")
            print(f"Bairro: {item.get('bairro')}")
            print(f"Cidade: {item.get('localidade')}")
            print(f"UF: {item.get('uf')}")
            print("-" * 40)
    else:
        print("Nenhum endereço encontrado.")
else:
    print("Nao houve sucesso na requisicao.")
