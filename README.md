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
```bash
python manage.py scrape_products
```

