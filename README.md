# Atividade Prática: Consumo de API Utilizando HTTP / GET

## Arquivos do Projeto

### **1) Atv1\_Consumo\_de\_API.py**

* Realiza uma requisição GET à API [ViaCEP](https://viacep.com.br/) usando um CEP específico.
* Retorna a resposta em **JSON**.
* Exibe o resultado no terminal.

### **2) Atv1\_Consumo\_de\_API\_XML.py**

* Versão do script que retorna o resultado da requisição **em XML**.
* Objetivo: praticar a manipulação de diferentes formatos de resposta.

### **3) Atv1\_Consumo\_de\_API\_LOOP.py**

* Consulta 5 CEPs **sequenciais** usando um loop:

  ```
  30140071, 30140072, 30140073, 30140074, 30140075
  ```
* Exibe os resultados de cada requisição no terminal.
* Pratica loops e construção dinâmica de URLs.

### **4) Atv1\_Consumo\_de\_API\_Endereco.py**

* Consulta a API ViaCEP usando **endereço completo** ao invés de CEP.
* Exemplo de URL: `viacep.com.br/ws/MG/Belo Horizonte/Rua dos Aimores/json/`
* Retorna uma lista de registros encontrados para o endereço informado.

### **5) Atv1\_Consumo\_de\_API\_ABC.py**

* Tenta acessar a URL `https://viacep.com.br/abc/`.
* Exibe o **código de retorno HTTP** (`status_code`) e o conteúdo da resposta.
* Objetivo: prática de tratamento de erros HTTP.

### **6) Atv1\_Consumo\_de\_API\_Result\_Google.py**

* Realiza uma pesquisa no Google via GET:

  ```
  http://www.google.com/search?q=elson de abreu
  ```
* Salva o resultado da pesquisa em um arquivo local chamado `resultado_google.html`.
* Pratica armazenamento de respostas em arquivos.

### **7) resultado\_google.html**

* Arquivo gerado pelo script `Atv1_Consumo_de_API_Result_Google.py`.
* Contém o HTML retornado da pesquisa no Google.

---

## Como Executar

1. Certifique-se de ter Python 3.x instalado.
2. Instale a biblioteca `requests` caso não tenha:

```bash
pip install requests
```

3. Execute os scripts conforme necessário:

```bash
python Atv1_Consumo_de_API.py
python Atv1_Consumo_de_API_XML.py
python Atv1_Consumo_de_API_LOOP.py
python Atv1_Consumo_de_API_Endereco.py
python Atv1_Consumo_de_API_ABC.py
python Atv1_Consumo_de_API_Result_Google.py
```

---

## Observações

* Todos os scripts estão configurados para exibir os resultados no terminal, exceto `Atv1_Consumo_de_API_Result_Google.py`, que salva em arquivo HTML.
* O objetivo da atividade é demonstrar consumo de APIs, manipulação de JSON/XML, loops e tratamento de respostas HTTP em Python.
