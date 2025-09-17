import requests

r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

if r.status_code == 200:
    print()
    print('Retorno : ', r.text)
    print()

    with open("resultado_google.html", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("Resultados salvos no arquivo 'resultado_google.html'")
else:
    print("Nao houve sucesso na requisicao.")
