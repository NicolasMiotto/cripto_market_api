# cripto_market_api
Repositório destinado para o desafio de integrar a API Coin Market CAP coletando os dados de cotações,
modelando-os e os armazenando em um banco de dados PostgreSQL.

## Instalação

1. Clone o repositório:

```sh
   git clone https://github.com/seuusuario/cripto-api-integration.git
   cd cripto-api-integration
```


2.Instale as dependências:

```sh
  pip install -r requirements.txt
```

3.Crie o arquivo env.py na raiz do projeto com as seguintes variáveis de ambiente:

```sh
  API_KEY='YOUR_API_KEY'
  DATABASE_URL='YOUR_DATABASE_URL'
```

4. Execute o arquivo criacoes_tabelas.sql para criar as tabelas necessárias no banco de dados.
Você pode fazer isso usando uma ferramenta como psql ou qualquer outro cliente PostgreSQL:

```sh
  criacao_tabelas.sql
```

5. Agora com tudo nos conformes, para rodar o script principal, tratar e armazenar os dados, estando dentro da pasta raiz do projeto execute:

 ```sh
  python main.py
```

6. Observação: Caso crie as tabelas com um nome diferente, altere o nome atual das tabelas nos parâmetros dos metodos de inserção
para o nome das tabelas do banco de dados que você decidiu nomear:
![image](https://github.com/user-attachments/assets/c7f93ce1-d9fb-4614-8bef-3c188223ed3d)


