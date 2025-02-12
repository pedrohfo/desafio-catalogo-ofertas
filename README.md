# Desafio Catálogo de Ofertas

Este projeto é um catálogo de ofertas que coleta produtos de um site de e-commerce e os exibe em uma interface web. Ele utiliza Django para o backend e Selenium para a coleta de dados.

## Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Git (para clonar o repositório)

## Configuração do Projeto

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/desafio-catalogo-ofertas.git
cd desafio-catalogo-ofertas
```

### 2. Criar e Ativar um Ambiente Virtual

No Linux/MacOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

O projeto utiliza PostgreSQL como banco de dados. Certifique-se de ter o PostgreSQL instalado e configurado.

Crie um banco de dados no PostgreSQL
```sql
CREATE DATABASE catalogo_ofertas;
```

Configure as credenciais do banco de dados no arquivo settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalogo_ofertas',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Execute as migrações para criar as tabelas no banco de dados:
```bash
python manage.py migrate
```

### 5. Coletar Dados dos Produtos
Baixe o Chrome Driver mais atualizado e compatível com seu Chrome,
e atualize o caminho do Chrome Driver no projeto, no arquivo scrape_products.py:

```python
        chrome_driver_path = r"C:\path\to\chromedriver.exe"
```

Para coletar os dados dos produtos, execute o comando de scraping:
```bash
python manage.py scrape_products
```
Este comando irá coletar os produtos do site e salvá-los no banco de dados.


### 6. Executar o Servidor

Inicie o servidor de desenvolvimento do Django:
```bash
python manage.py runserver
```

Acesse o projeto no navegador em:
```
http://127.0.0.1:8000/products/
```
