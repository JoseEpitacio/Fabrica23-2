## Desafio Fábrica
<h1 align="center">CRUD Livraria</h1>

## Descrição do Projeto
<p align="center">CRUD simples de uma Livraria para o desafio final do workshop de back-end para a Fábrica de Software Unipê. O projeto consiste num CRUD entre duas entidades (Livro e Autor), fazendo um relacionamento n:n entre os dois</p>

<p align="center">
 <a href="#objetivo">Pré-Requisitos</a> • 
 <a href="#tecnologias">Execução</a> • 
 <a href="#tecnologias">Criação de Entidades</a> • 
 <a href="#contribuicao">Autor</a> • 
</p>

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/downloads/), [Postgresql](https://www.postgresql.org/download/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### 🎲 Rodando o Back End (servidor)

```bash
# Clone este repositório
$ git clone <https://github.com/JoseEpitacio/Fabrica23-2.git>
```

# No terminal crie seu virtual enviroment
python -m venv venv

# Instale as dependências
pip install -r ./requirements.txt

# Crie um banco em POSTGRESQL
Crie um banco no PSQL e configure a conexão no settings.py

# Execução
Após todos os pré-requisitos instalados, execute a aplicação com 'python ./manage.py runserver'

# Criação de Entidades
Para criar os Autores e os Livros acesse localhost:8000/admin e crie o seu superuser com 'python ./manage.py createsuperuser'

# Autor [JoseEpitacio](https://github.com/JoseEpitacio/)
