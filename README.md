📊 Organizador Financeiro Web com Django

Sistema web profissional para controle financeiro pessoal, desenvolvido com Django, Django REST Framework, autenticação JWT e Dashboard com gráficos.

Este projeto permite o cadastro de receitas, despesas, categorias e apresenta um resumo financeiro visual através de um dashboard interativo.

🚀 Tecnologias Utilizadas

Python 3

Django

Django REST Framework

JWT Authentication

Chart.js

HTML / CSS

SQLite (padrão Django)

Git / GitHub

🎯 Funcionalidades

Cadastro de categorias

Cadastro de receitas e despesas

Associação das transações por usuário

Dashboard financeiro

Gráfico de receitas e despesas

API REST protegida com JWT

Sistema multiusuário

Autenticação segura

Estrutura pronta para frontend React

📂 Estrutura do Projeto
financeiro/
 ├ core/
 │   ├ models.py
 │   ├ views.py
 │   ├ api.py
 │   ├ serializers.py
 │   ├ urls.py
 │   └ templates/
 ├ financeiro/
 │   ├ settings.py
 │   ├ urls.py
 │   └ wsgi.py
 └ manage.py

⚙️ Como rodar o projeto localmente
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate

3. Instale as dependências
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install djangorestframework-simplejwt

4. Rode as migrações
python manage.py makemigrations
python manage.py migrate

5. Crie o superusuário
python manage.py createsuperuser

6. Inicie o servidor
python manage.py runserver


Acesse:

http://127.0.0.1:8000/


Admin:

http://127.0.0.1:8000/admin

🔐 Autenticação JWT

Endpoint:

POST /api/token/


Body:

{
  "username": "usuario",
  "password": "senha"
}


Resposta:

{
  "access": "token",
  "refresh": "token"
}


Use o token:

Authorization: Bearer SEU_TOKEN

📊 Dashboard

O dashboard exibe:

Total de receitas

Total de despesas

Saldo

Gráfico de pizza

📌 Próximas melhorias

Frontend em React

App Mobile

Exportação para Excel

Relatórios mensais

Deploy em nuvem

Sistema SaaS

👨‍💻 Autor

Luiz Fernando

Projeto desenvolvido para fins de aprendizado, portfólio e demonstração de habilidades em desenvolvimento web backend com Django.
