# Backend sala de leitura

## Introdução Sala de leitura

Sala de leitura é um sistema para gerenciamento e catalogação de livros para bibliotecas.
A ideia surgiu da materia de Projeto Integrador dos alunos do eixo computação da UNIVESP (Universidade Virtual do Estado de São Paulo). 

## pre requisitos para rodar

```
    python 3
    pip
    mysql
```


## Como rodar localmente

Faça um git clone do projeto.

Após clonar o projeto em sua maquina, entre na pasta do projeto

``` 
cd backend-saladeleitura
```

Crie um ambiente virtual que será onde vamos rodar a aplicação.

```Linux 
python3 -m venv env
source env/bin/activate
```
```Windows 
python3 -m venv env
source env/script/activate
```

Você verá que o terminal estará um pouco diferente de antes o que significa que voce estará no ambiente virtual.

Feito isso instale as dependencias com o seguinte comando.

``` 
pip install -r requirements.txt
```

Após a conclusão da instalação abra a pasta backend e edite o arquivo config_database.py colocando seu usuario e senha do banco de dados mysql.

Abra o mysql e crie um banco de dados chamado saladeleitura.

``` 
create database saladeleitura;
```

Agora volte ao backend-saladeleitura e rode os comandos:

``` 
python3 manage.py makemigrations Libraryapp   
python3 manage.py migrate Libraryapp 
```

Feito isso o banco estara populado com as tabelas e você já poderá realizar suas consultas nele.

Para rodar a aplicação basta apenas rodar:

``` 
python manage.py runserver
```

pronto agora a aplicação já estará rodando na:

```
http://127.0.0.1:8000/
```